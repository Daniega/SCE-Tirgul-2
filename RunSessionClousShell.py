from cloudshell.api.cloudshell_api import CloudShellAPISession, AppConfiguration

session = CloudShellAPISession('localhost', "admin", "admin", "Global")
session.ConfigureApps(reservationId='bd848aeb-c2ec-44fc-9a8f-5944bf22f3da',appConfigurations=[AppConfiguration('app-name', None)])
