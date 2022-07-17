def page_2__view_run_lists(state):
    import streamlit as st

    st.markdown("# Run Lists 🎈")
    # 1: Iterate through all the requests in the state.
    for i, r in enumerate(state.requests):
        i = str(i)
        # 2: Display information such as request, logs, work state, model score.
        work = state._state["structures"]["ws"]["works"][f"w_{i}"]
        with st.expander(f"Expand to view Run {i}", expanded=False):
            if st.checkbox(f"Expand to view your configuration", key=i):
                st.json(r)
            if st.checkbox(f"Expand to view logs", key=i):
                st.code(body=work["vars"]["logs"])
            if st.checkbox(f"Expand to view your work state", key=i):
                work["vars"].pop("logs")
                st.json(work)
            best_model_score = r.get("best_model_score", None)
            if best_model_score:
                if st.checkbox(f"Expand to view your run performance", key=i):
                    st.json({"best_model_score": best_model_score, "best_model_path": r.get("best_model_path")})
