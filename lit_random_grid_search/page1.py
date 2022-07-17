
def page_1__create_new_run(state):
    import streamlit as st

    st.markdown("# Create a new Run 🎈")

    # 1: Collect arguments from the users
    id = st.text_input("Name your run", value="my_first_run")
    github_repo = st.text_input(
        "Enter a Github Repo URL", value="https://github.com/Lightning-AI/lightning-quick-start.git"
    )

    default_script_args = "--trainer.max_epochs=5 --trainer.limit_train_batches=4 --trainer.limit_val_batches=4 --trainer.callbacks=ModelCheckpoint --trainer.callbacks.monitor=val_acc"
    default_requirements = "torchvision, pytorch_lightning, jsonargparse[signatures]"

    script_path = st.text_input("Enter your script to run", value="train_script.py")
    script_args = st.text_input("Enter your base script arguments", value=default_script_args)
    requirements = st.text_input("Enter your requirements", value=default_requirements)
    ml_framework = st.radio("Select your ML Training Frameworks", options=["PyTorch Lightning", "Keras", "Tensorflow"])

    if ml_framework not in ("PyTorch Lightning"):
        st.write(f"{ml_framework} isn't supported yet.")
        return

    clicked = st.button("Submit")

    # 2: If clicked, create a new request.
    if clicked:
        new_request = {
            "id": id,
            "train": {
                "github_repo": github_repo,
                "script_path": script_path,
                "script_args": script_args.split(" "),
                "requirements": requirements.split(" "),
                "ml_framework": ml_framework,
            },
        }
        # 3: IMPORTANT: Add a new request to the state in-place.
        # The flow receives the UI request and dynamically create
        # and run the associated work from the request information.
        state.requests = state.requests + [new_request]
