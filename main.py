# Before running, a 'credentials.json' file needs to be created for this app.
# And all environment variables need to be replaced.
# Environment Variables = [auth_system.py > MY_EMAIL, MY_EMAIL_PASSWORD, program_manager.py > TIMEZONEDB_API_KEY]

import program_manager as manager
import auth_system as auth
import convert_interface as CI
import world_interface as WI
import profile_interface as PI
import ui

# Variable to check if the user is already in the app
in_app = False

# Set commands
ui.login_btn.config(command=lambda : auth.log_in([ui.login_user_entry.get(), ui.login_pass_entry.get()]))
ui.continue_btn.config(command=auth.verify)

ui.convert_button.config(command=lambda : CI.main([WI.main_canvas, PI.main_canvas]))
ui.world_button.config(command=lambda : WI.main([CI.main_canvas, PI.main_canvas]))
ui.profile_button.config(command=lambda : PI.main([CI.main_canvas, WI.main_canvas]))

# Main Loop
while True:
    ui.window.update()

    # If the user is authenticated but not in app, let the user log in
    if auth.authenticated is True and in_app is not True:
        PI.username_label.config(text=f"Username : {auth.user_data['Username']}")
        PI.pwd_label.config(text=f"Password : {auth.user_data['Password']}")
        PI.email_label.config(text=f"Email : {auth.user_data['Email']}")
        ui.home()
        PI.main([WI.main_canvas])
        in_app = True
    
    # If the user is in app, start running the clocks
    if in_app:
        manager.update_clocks()