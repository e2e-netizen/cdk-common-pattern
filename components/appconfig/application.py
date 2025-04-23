from aws_cdk import aws_appconfig as appconfig
from constructs import Construct

def create_application(scope: Construct, id: str, app: dict) -> appconfig.CfnApplication:
    return appconfig.CfnApplication(scope, id,
        name=app["name"],
        description=app.get("description", "")
    )
