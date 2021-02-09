import os

import hypothesis
from dotenv import load_dotenv

# load environments variable from file
load_dotenv()

suppress_health_check = (
    hypothesis.HealthCheck.data_too_large,
    hypothesis.HealthCheck.filter_too_much,
    hypothesis.HealthCheck.too_slow,
    hypothesis.HealthCheck.return_value,
    hypothesis.HealthCheck.large_base_example,
    hypothesis.HealthCheck.not_a_test_method,
)

# CREATE CI PROFILE
# =================
hypothesis.settings.register_profile(
    "ci",
    deadline=1000,
    max_examples=1000,
    suppress_health_check=suppress_health_check,
)

# CREATE DEBUGGING PROFILE
# ========================
hypothesis.settings.register_profile(
    "debug",
    deadline=1000,
    max_examples=20,
    suppress_health_check=suppress_health_check,
    verbosity=hypothesis.Verbosity.verbose,
)

# SET PROFILE
# ===========
# read value from TESTING_PROFILE environment variable
MODE = os.environ.get("TESTING_PROFILE", "debug")
hypothesis.settings.load_profile(MODE)
