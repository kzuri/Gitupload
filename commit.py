import subprocess as cmd

cmd.check_output("git add .",shell=True)

response = input("Do you want to use the default message for this commit?([y]/n)\n")
message = "update the repository"

if response.startswith('n'):
    message = input("What message you want?\n")

cmd.check_output(f"git commit -m '{message}'",shell=True)
cmd.check_output("git push -u origin master -f", shell=True)
