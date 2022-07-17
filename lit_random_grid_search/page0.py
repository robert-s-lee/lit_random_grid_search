def render_fn(state: AppState):
    import streamlit as st

    page_names_to_funcs = {
        "Create a new Run": partial(page_1__create_new_run, state=state),
        "View your Runs": partial(page_2__view_run_lists, state=state),
        "View the App state": partial(page_3__view_app_state, state=state),
    }
    selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
    page_names_to_funcs[selected_page]()