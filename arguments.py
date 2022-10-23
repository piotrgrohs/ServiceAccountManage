
import getopt
import sys
from classes.serviceAccount import list_of_serviceAccount
from classes.serviceAccount import serviceAccount


# Remove 1st argument from the
# list of command line arguments
argumentList = sys.argv[1:]

# Options
options = "hf:dalp:i:t:"

# Long options
long_options = ["Help", "File=", "Delete=", "Add", "List", "Project=", "App=", "Id="]

try:
    # Parsing argument
    arguments, values = getopt.getopt(argumentList, options, long_options)
    list_of_serviceAccount = list_of_serviceAccount()
    serviceAccount = serviceAccount()
    serviceAccount.id = -1
    # checking each argument
    for currentArgument, currentValue in arguments:

        if currentArgument in ("-h", "--Help"):
            print("Displaying Help")

        elif currentArgument in ("-f", "--File"):
            list_of_serviceAccount.file = currentValue
            list_of_serviceAccount.load()

        elif currentArgument in ("-d", "--Delete"):
            # Delete service account
            # arguments.py -p 'test2' -i '0' -d 
            list_of_serviceAccount.load()
            if serviceAccount.project == '':
                raise TypeError('Project not set -p')
            project = serviceAccount.project
            if serviceAccount.id < 0: 
                raise TypeError('Service Account not set -i')
            list_of_serviceAccount.delete(serviceAccount.id,project)
            list_of_serviceAccount.save()

        elif currentArgument in ("-a", "--Add"):
            # Add service account
            # arguments.py -t 'test' -p 'test2' -aś
            list_of_serviceAccount.load()
            project = serviceAccount.project
            app = serviceAccount.app
            description = serviceAccount.description
            serviceAccount.check()

            list_of_serviceAccount.add(app, project, description)
            list_of_serviceAccount.save()

        elif currentArgument in ("-p", "--Project"):
            # Set project
            serviceAccount.project = currentValue

        elif currentArgument in ("-t", "--App"):
            # Set project
            serviceAccount.app = currentValue
        
        elif currentArgument in ("-i", "--Id"):
            # Set project
            serviceAccount.id = int(currentValue)

        elif currentArgument in ("-l", "--List"):
            # List service accounts
            if len(list_of_serviceAccount.list) < 1:
                list_of_serviceAccount.load()
            list_of_serviceAccount.show()
            pass

except getopt.error as err:
    # output error, and return with an error code
    print(str(err))
