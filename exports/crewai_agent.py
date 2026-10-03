from crewai import Agent

carbon_satellite_verification_node = Agent(
    role="Carbon Satellite Verification Node",
    goal="Deliver high-precision autonomous Carbon Satellite Verification Node operations",
    backstory="Engineered under OpenGAP governance standards.",
    verbose=True,
    allow_delegation=False
)
