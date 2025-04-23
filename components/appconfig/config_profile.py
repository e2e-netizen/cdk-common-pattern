from aws_cdk import aws_appconfig as appconfig
from constructs import Construct

def create_config_profile(scope: Construct, id: str, app_id: str, profile: dict) -> appconfig.CfnConfigurationProfile:
    return appconfig.CfnConfigurationProfile(scope, id,
        application_id=app_id,
        name=profile["name"],
        location_uri="hosted",
        description=profile.get("description", "")
    )
