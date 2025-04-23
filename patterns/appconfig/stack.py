from aws_cdk import Stack
from constructs import Construct
from cdk_common_patterns.components.appconfig.application import create_application
from cdk_common_patterns.components.appconfig.config_profile import create_config_profile
from cdk_common_patterns.components.appconfig.vars import AppConfigInput
from cdk_common_patterns.components.appconfig.outputs import AppConfigOutputs

class AppConfigPattern(Stack):
    def __init__(self, scope: Construct, construct_id: str, app_config: AppConfigInput, **kwargs):
        super().__init__(scope, construct_id, **kwargs)

        app = app_config["applications"][0]  # assuming single app for now

        application = create_application(self, "AppConfigApp", app)

        freeform = create_config_profile(self, "FreeformProfile", application.ref, app["freeform_config_profile"])
        feature_flag = create_config_profile(self, "FeatureFlagProfile", application.ref, app["feature_flag_config_profile"])

        self.outputs: AppConfigOutputs = {
            "application_id": application.ref,
            "application_arn": application.attr_arn,
            "config_profile_arns": [freeform.attr_arn, feature_flag.attr_arn],
            "environment_ids": [],
            "cross_account_role_arn": None,
        }
