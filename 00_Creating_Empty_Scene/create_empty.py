
# Argparse is used in isaac lab App launcher hence is used for user input.
import argparse

from omni.isaac.lab.app import AppLauncher


# Create argparser
parser = argparse.ArgumentParser(description="Creating empty space tutorial.")

# Pass 'parser' to app launcher
AppLauncher.add_app_launcher_args(parser)

# Parse args
args_cli = parser.parse_args()


# Launcher omniverse app
app_launcher = AppLauncher(args_cli)
simulation_app = app_launcher.app


'''
 When running isaacsim via standalone script the "Simulatino Context" handels
 all timeliyne events (pause, start, etc).
 '''

from omni.isaac.lab.sim import SimulationCfg, SimulationContext

#############################
#       Running sim         #
#############################

def main():
    # Set simulation context
    sim_cfg = SimulationCfg(dt=0.01)
    sim     = SimulationContext(sim_cfg)
        # Simulation context configs device, gravity vector, solver param

    # Set main set_camera_view
    sim.set_camera_view([2.5, 2.5, 2.5], [0., 0., 0.])

    sim.reset()
    # sim.SimulationContext.reset() Do Not Use
        # Must be called at start of every simulation to reset env params

    print("[INFO]: Setup Complete...")

    # Start physics simulation
    while simulation_app.is_running():
        # Perform time step
        sim.step()



if __name__ == "__main__":
    # run the main function
    main()
    # close sim app
    simulation_app.close()
