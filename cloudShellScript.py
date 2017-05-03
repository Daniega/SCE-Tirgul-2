from cloudshell.api.cloudshell_api import CloudShellAPISession, AppConfiguration

session = CloudShellAPISession('localhost', "admin", "admin", "Global")
session.ConfigureApps(reservationId='a47ba512-ad70-439e-8375-ec27c0e5c7a2',appConfigurations=[AppConfiguration('Dani-Illya-Daniel Kosher App', None)])
