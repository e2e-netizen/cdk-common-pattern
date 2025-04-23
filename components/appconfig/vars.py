from typing import TypedDict, Optional, List

class AppConfigProfile(TypedDict):
    name: str
    description: Optional[str]

class AppConfigEnvironment(TypedDict):
    name: str
    description: Optional[str]

class AppConfigApp(TypedDict):
    name: str
    description: Optional[str]
    freeform_config_profile: AppConfigProfile
    feature_flag_config_profile: AppConfigProfile
    environments: Optional[List[AppConfigEnvironment]]
    trusted_accounts: Optional[List[str]]

class AppConfigInput(TypedDict):
    deployment_strategy_id: str
    applications: List[AppConfigApp]
