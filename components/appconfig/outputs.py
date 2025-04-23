from typing import TypedDict, List, Optional

class AppConfigOutputs(TypedDict):
    application_id: str
    application_arn: str
    config_profile_arns: List[str]
    environment_ids: List[str]
    cross_account_role_arn: Optional[str]
