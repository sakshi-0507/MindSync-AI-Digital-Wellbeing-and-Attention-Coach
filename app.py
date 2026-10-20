
# from pathlib import Path

# import joblib
# import pandas as pd
# import streamlit as st


# # --------------------------------------------------
# # 1. PAGE CONFIGURATION
# # --------------------------------------------------

# st.set_page_config(
#     page_title="MindSync AI",
#     page_icon="🧠",
#     layout="wide"
# )


# # --------------------------------------------------
# # 2. LOAD EXISTING TRAINED MODEL
# # --------------------------------------------------

# MODEL_PATH = (
#     Path(__file__).resolve().parent
#     / "mindsync_models"
#     / "mindsync_model_bundle.joblib"
# )


# @st.cache_resource
# def load_model_bundle():
#     return joblib.load(MODEL_PATH)


# if not MODEL_PATH.exists():
#     st.error(f"Model bundle not found: {MODEL_PATH}")
#     st.info(
#         "Check that the mindsync_models folder is "
#         "in the same directory as app.py."
#     )
#     st.stop()

# try:
#     bundle = load_model_bundle()

#     model = bundle["model"]
#     scaler = bundle["scaler"]
#     FEATURES = bundle["features"]
#     CATEGORIES = bundle["categories"]

# except Exception as error:
#     st.error(f"Could not load model bundle: {error}")
#     st.stop()


# # --------------------------------------------------
# # 3. APP HEADER
# # --------------------------------------------------

# st.title("🧠 MindSync AI")

# st.subheader(
#     "Your Personalized Digital Wellbeing and Attention Coach"
# )

# st.write(
#     "Explore your digital habits, estimate your risk category, "
#     "and discover practical ways to build healthier routines."
# )

# st.success("Existing trained model loaded successfully.")

# with st.expander("Model information"):
#     st.write("Model:", type(model).__name__)
#     st.write("Required features:", len(FEATURES))
#     st.write("Prediction classes:", list(model.classes_))


# # --------------------------------------------------
# # 4. PERSONALIZED SUGGESTIONS
# # --------------------------------------------------

# def get_recommendations(d):
#     tips = []

#     if d["Daily_Usage_Hours"] >= 6:
#         tips.append(
#             "Try reducing daily phone use gradually, "
#             "starting with 30 minutes less per day."
#         )

#     if d["Sleep_Hours"] < 7:
#         tips.append(
#             "Protect your sleep schedule and consider "
#             "keeping your phone away from your bed."
#         )

#     if d["Screen_Time_Before_Bed"] >= 1:
#         tips.append(
#             "Try a screen-free wind-down period before bedtime."
#         )

#     if d["Phone_Checks_Per_Day"] >= 80:
#         tips.append(
#             "Turn off non-essential notifications and check "
#             "your phone at planned times."
#         )

#     if d["Time_on_Social_Media"] >= 3:
#         tips.append(
#             "Try app timers or planned breaks from social media."
#         )

#     if d["Time_on_Gaming"] >= 2:
#         tips.append(
#             "Set planned gaming periods and take regular breaks."
#         )

#     if d["Apps_Used_Daily"] >= 8:
#         tips.append(
#             "Review your daily apps and mute notifications "
#             "from those that are not important."
#         )

#     if d["Exercise_Hours"] < 0.5:
#         tips.append(
#             "Consider adding a short walk or another enjoyable "
#             "offline activity to your routine."
#         )

#     if d["Social_Interactions"] <= 3:
#         tips.append(
#             "Make time for a conversation or an activity "
#             "with friends or family."
#         )

#     if d["Weekend_Usage_Hours"] >= 7:
#         tips.append(
#             "Plan one or two offline activities for the weekend."
#         )

#     if not tips:
#         tips.append(
#             "Keep maintaining a balance between screen time, "
#             "sleep, physical activity, and offline time."
#         )

#     return tips[:6]


# # --------------------------------------------------
# # 5. MAIN INPUT FORM: ALL 20 FEATURES
# # --------------------------------------------------

# with st.form("mindsync_inputs"):

#     st.header("1. About You")

#     col1, col2 = st.columns(2)

#     age = col1.number_input(
#         "Age",
#         min_value=10,
#         max_value=100,
#         value=24
#     )

#     gender = col2.selectbox(
#         "Gender",
#         list(CATEGORIES["Gender"].keys())
#     )

#     st.header("2. Digital Habits")

#     col1, col2 = st.columns(2)

#     daily = col1.number_input(
#         "Daily phone usage (hours)",
#         min_value=0.0,
#         max_value=24.0,
#         value=5.0,
#         step=0.5
#     )

#     weekend = col2.number_input(
#         "Weekend phone usage (hours/day)",
#         min_value=0.0,
#         max_value=24.0,
#         value=6.0,
#         step=0.5
#     )

#     social = col1.number_input(
#         "Social media (hours/day)",
#         min_value=0.0,
#         max_value=24.0,
#         value=2.0,
#         step=0.5
#     )

#     gaming = col2.number_input(
#         "Gaming (hours/day)",
#         min_value=0.0,
#         max_value=24.0,
#         value=1.0,
#         step=0.5
#     )

#     education = col1.number_input(
#         "Educational phone use (hours/day)",
#         min_value=0.0,
#         max_value=24.0,
#         value=1.0,
#         step=0.5
#     )

#     checks = col2.number_input(
#         "Phone checks per day",
#         min_value=0,
#         max_value=1000,
#         value=50
#     )

#     apps = col1.number_input(
#         "Apps used daily",
#         min_value=0,
#         max_value=100,
#         value=6
#     )

#     purpose = col2.selectbox(
#         "Main purpose of phone use",
#         list(CATEGORIES["Phone_Usage_Purpose"].keys())
#     )

#     before_bed = col1.number_input(
#         "Screen time before bed (hours)",
#         min_value=0.0,
#         max_value=8.0,
#         value=1.0,
#         step=0.5
#     )

#     st.header("3. Lifestyle and Wellbeing")

#     col1, col2 = st.columns(2)

#     sleep = col1.number_input(
#         "Sleep (hours/night)",
#         min_value=0.0,
#         max_value=14.0,
#         value=7.0,
#         step=0.5
#     )

#     exercise = col2.number_input(
#         "Exercise (hours/day)",
#         min_value=0.0,
#         max_value=8.0,
#         value=0.5,
#         step=0.5
#     )

#     interactions = col1.slider(
#         "Social interactions (0–10)",
#         min_value=0,
#         max_value=10,
#         value=5
#     )

#     family = col2.slider(
#         "Family communication (0–10)",
#         min_value=0,
#         max_value=10,
#         value=5
#     )

#     academic = col1.slider(
#         "Academic performance (0–100)",
#         min_value=0,
#         max_value=100,
#         value=75
#     )

#     parental = col2.selectbox(
#         "Parental controls",
#         ["No", "Yes"]
#     )

#     st.subheader("Additional Model Inputs")

#     col1, col2 = st.columns(2)

#     anxiety = col1.slider(
#         "Anxiety level (0–10)",
#         min_value=0,
#         max_value=10,
#         value=3
#     )

#     depression = col2.slider(
#         "Depression level (0–10)",
#         min_value=0,
#         max_value=10,
#         value=3
#     )

#     self_esteem = col1.slider(
#         "Self-esteem (0–10)",
#         min_value=0,
#         max_value=10,
#         value=7
#     )

#     submitted = st.form_submit_button(
#         "Predict My Risk",
#         type="primary",
#         use_container_width=True
#     )


# # --------------------------------------------------
# # 6. SAVE THE SUBMITTED BASELINE
# # --------------------------------------------------

# if "baseline_values" not in st.session_state:
#     st.session_state.baseline_values = None


# if submitted:

#     st.session_state.baseline_values = {
#         "Age": age,
#         "Gender": CATEGORIES["Gender"][gender],
#         "Daily_Usage_Hours": daily,
#         "Sleep_Hours": sleep,
#         "Academic_Performance": academic,
#         "Social_Interactions": interactions,
#         "Exercise_Hours": exercise,
#         "Anxiety_Level": anxiety,
#         "Depression_Level": depression,
#         "Self_Esteem": self_esteem,
#         "Parental_Control": 1 if parental == "Yes" else 0,
#         "Screen_Time_Before_Bed": before_bed,
#         "Phone_Checks_Per_Day": checks,
#         "Apps_Used_Daily": apps,
#         "Time_on_Social_Media": social,
#         "Time_on_Gaming": gaming,
#         "Time_on_Education": education,
#         "Phone_Usage_Purpose": (
#             CATEGORIES["Phone_Usage_Purpose"][purpose]
#         ),
#         "Family_Communication": family,
#         "Weekend_Usage_Hours": weekend
#     }

#     # Reset simulator controls to the newly submitted habits.
#     # This is done before the simulator widgets are created.
#     st.session_state["sim_daily"] = float(daily)
#     st.session_state["sim_social"] = float(social)
#     st.session_state["sim_gaming"] = float(gaming)
#     st.session_state["sim_sleep"] = float(sleep)
#     st.session_state["sim_exercise"] = float(exercise)
#     st.session_state["sim_bed"] = float(before_bed)


# # --------------------------------------------------
# # 7. BASELINE PREDICTION
# # --------------------------------------------------

# baseline_values = st.session_state.baseline_values


# if baseline_values is not None:

#     baseline_df = pd.DataFrame(
#         [baseline_values]
#     )[FEATURES]

#     baseline_scaled = scaler.transform(baseline_df)

#     baseline_prediction = str(
#         model.predict(baseline_scaled)[0]
#     )

#     baseline_probabilities = model.predict_proba(
#         baseline_scaled
#     )[0]

#     baseline_confidence = dict(
#         zip(model.classes_, baseline_probabilities)
#     )

#     st.divider()
#     st.header("Your MindSync Results")

#     if baseline_prediction == "High":
#         st.error(
#             f"Predicted risk category: {baseline_prediction}"
#         )
#     elif baseline_prediction == "Medium":
#         st.warning(
#             f"Predicted risk category: {baseline_prediction}"
#         )
#     else:
#         st.success(
#             f"Predicted risk category: {baseline_prediction}"
#         )

#     st.caption(
#         "These probabilities are model estimates, not a medical "
#         "diagnosis or a guarantee of prediction accuracy."
#     )

#     st.subheader("Prediction Probability Scores")

#     for label in ["High", "Medium", "Low"]:
#         if label in baseline_confidence:
#             st.progress(
#                 float(baseline_confidence[label]),
#                 text=(
#                     f"{label}: "
#                     f"{baseline_confidence[label]:.1%}"
#                 )
#             )

#     st.subheader("Your Personalized Suggestions")

#     for tip in get_recommendations(baseline_values):
#         st.markdown(f"- {tip}")

#     st.info(
#         "MindSync AI provides estimates from your existing trained "
#         "model. Suggestions are rule-based and are not medical "
#         "or psychological advice."
#     )


#     # --------------------------------------------------
#     # 8. WHAT-IF HABIT SIMULATOR
#     # --------------------------------------------------

#     st.divider()
#     st.header("What-If Habit Simulator")

#     st.write(
#         "Change selected habits below to explore how the model's "
#         "predicted risk category and probability scores may change. "
#         "Your original submitted inputs remain unchanged."
#     )

#     # Initialize simulator controls on their first appearance.
#     simulator_defaults = {
#         "sim_daily": float(
#             baseline_values["Daily_Usage_Hours"]
#         ),
#         "sim_social": float(
#             baseline_values["Time_on_Social_Media"]
#         ),
#         "sim_gaming": float(
#             baseline_values["Time_on_Gaming"]
#         ),
#         "sim_sleep": float(
#             baseline_values["Sleep_Hours"]
#         ),
#         "sim_exercise": float(
#             baseline_values["Exercise_Hours"]
#         ),
#         "sim_bed": float(
#             baseline_values["Screen_Time_Before_Bed"]
#         )
#     }

#     for key, default_value in simulator_defaults.items():
#         if key not in st.session_state:
#             st.session_state[key] = default_value

#     st.subheader("Adjust Your Habits")

#     col1, col2 = st.columns(2)

#     with col1:

#         sim_daily = st.slider(
#             "Daily phone usage (hours)",
#             min_value=0.0,
#             max_value=24.0,
#             step=0.5,
#             key="sim_daily"
#         )

#         sim_social = st.slider(
#             "Social media (hours/day)",
#             min_value=0.0,
#             max_value=24.0,
#             step=0.5,
#             key="sim_social"
#         )

#         sim_gaming = st.slider(
#             "Gaming (hours/day)",
#             min_value=0.0,
#             max_value=24.0,
#             step=0.5,
#             key="sim_gaming"
#         )

#     with col2:

#         sim_sleep = st.slider(
#             "Sleep (hours/night)",
#             min_value=0.0,
#             max_value=14.0,
#             step=0.5,
#             key="sim_sleep"
#         )

#         sim_exercise = st.slider(
#             "Exercise (hours/day)",
#             min_value=0.0,
#             max_value=8.0,
#             step=0.5,
#             key="sim_exercise"
#         )

#         sim_bed = st.slider(
#             "Screen time before bed (hours)",
#             min_value=0.0,
#             max_value=8.0,
#             step=0.5,
#             key="sim_bed"
#         )

#     # Start with the saved baseline, not the form's current widgets.
#     what_if_values = baseline_values.copy()

#     # Change only the six habits selected in the simulator.
#     what_if_values["Daily_Usage_Hours"] = sim_daily
#     what_if_values["Time_on_Social_Media"] = sim_social
#     what_if_values["Time_on_Gaming"] = sim_gaming
#     what_if_values["Sleep_Hours"] = sim_sleep
#     what_if_values["Exercise_Hours"] = sim_exercise
#     what_if_values["Screen_Time_Before_Bed"] = sim_bed

#     # Preserve the exact training feature order.
#     what_if_df = pd.DataFrame(
#         [what_if_values]
#     )[FEATURES]

#     what_if_scaled = scaler.transform(what_if_df)

#     what_if_prediction = str(
#         model.predict(what_if_scaled)[0]
#     )

#     what_if_probabilities = model.predict_proba(
#         what_if_scaled
#     )[0]

#     what_if_confidence = dict(
#         zip(model.classes_, what_if_probabilities)
#     )

#     # --------------------------------------------------
#     # 9. COMPARE BASELINE AND WHAT-IF RESULTS
#     # --------------------------------------------------

#     st.subheader("Before vs. After")

#     metric1, metric2 = st.columns(2)

#     metric1.metric(
#         "Current predicted category",
#         baseline_prediction
#     )

#     metric2.metric(
#         "What-if predicted category",
#         what_if_prediction
#     )

#     if baseline_prediction != what_if_prediction:
#         st.success(
#             f"The predicted category changed from "
#             f"{baseline_prediction} to {what_if_prediction}."
#         )
#     else:
#         st.info(
#             "The predicted category remains the same for these "
#             "adjustments. Check the probability comparison below "
#             "for smaller changes in the model's estimates."
#         )

#     labels = ["High", "Medium", "Low"]

#     probability_comparison = pd.DataFrame(
#         {
#             "Current habits": [
#                 baseline_confidence.get(label, 0.0)
#                 for label in labels
#             ],
#             "What-if habits": [
#                 what_if_confidence.get(label, 0.0)
#                 for label in labels
#             ]
#         },
#         index=labels
#     )

#     st.subheader("Risk Probability Comparison")

#     st.bar_chart(probability_comparison)

#     display_comparison = probability_comparison.copy()

#     display_comparison["Current habits"] = (
#         display_comparison["Current habits"].map(
#             lambda x: f"{x:.1%}"
#         )
#     )

#     display_comparison["What-if habits"] = (
#         display_comparison["What-if habits"].map(
#             lambda x: f"{x:.1%}"
#         )
#     )

#     st.dataframe(
#         display_comparison,
#         use_container_width=True
#     )

#     # --------------------------------------------------
#     # 10. SHOW WHAT CHANGED
#     # --------------------------------------------------

#     st.subheader("Your Habit Adjustments")

#     habit_changes = [
#         (
#             "Daily phone usage",
#             "Daily_Usage_Hours",
#             sim_daily,
#             "hours/day"
#         ),
#         (
#             "Social media",
#             "Time_on_Social_Media",
#             sim_social,
#             "hours/day"
#         ),
#         (
#             "Gaming",
#             "Time_on_Gaming",
#             sim_gaming,
#             "hours/day"
#         ),
#         (
#             "Sleep",
#             "Sleep_Hours",
#             sim_sleep,
#             "hours/night"
#         ),
#         (
#             "Exercise",
#             "Exercise_Hours",
#             sim_exercise,
#             "hours/day"
#         ),
#         (
#             "Screen time before bed",
#             "Screen_Time_Before_Bed",
#             sim_bed,
#             "hours"
#         )
#     ]

#     changes_found = False

#     for name, feature, adjusted_value, unit in habit_changes:

#         original_value = float(baseline_values[feature])

#         if adjusted_value != original_value:
#             changes_found = True

#             difference = adjusted_value - original_value

#             st.write(
#                 f"- **{name}:** {original_value:g} → "
#                 f"{adjusted_value:g} {unit} "
#                 f"({difference:+g})"
#             )

#     if not changes_found:
#         st.write(
#             "No habits have been changed yet. Move a slider "
#             "to explore a different scenario."
#         )

#     st.subheader("Suggestions for Your Adjusted Habits")

#     adjusted_tips = get_recommendations(what_if_values)

#     for tip in adjusted_tips:
#         st.markdown(f"- {tip}")

#     st.caption(
#         "What-if results are hypothetical model estimates. "
#         "They do not prove that changing a habit will cause a "
#         "particular outcome. This tool is not a medical assessment."
#     )
    
#     # --------------------------------------------------
#     # STEP 4: DIGITAL ATTENTION BUDGET
#     # --------------------------------------------------

#     st.divider()
#     st.header("Digital Attention Budget")

#     st.write(
#         "Set a daily recreational phone-use budget and see "
#         "how your current habits compare with your goal."
#     )

#     attention_budget = st.slider(
#         "Your daily recreational phone-use budget (hours)",
#         min_value=1.0,
#         max_value=12.0,
#         value=3.0,
#         step=0.5,
#         key="attention_budget"
#     )

#     current_usage = float(
#         baseline_values["Daily_Usage_Hours"]
#     )

#     remaining_time = attention_budget - current_usage

#     metric1, metric2, metric3 = st.columns(3)

#     metric1.metric(
#         "Current daily phone use",
#         f"{current_usage:.1f} hours"
#     )

#     metric2.metric(
#         "Your daily budget",
#         f"{attention_budget:.1f} hours"
#     )

#     metric3.metric(
#         "Budget remaining",
#         f"{max(remaining_time, 0):.1f} hours"
#     )

#     if remaining_time > 0:
#         st.success(
#             f"You are {remaining_time:.1f} hours below your "
#             "chosen daily budget."
#         )

#     elif remaining_time == 0:
#         st.info(
#             "You are exactly at your chosen daily budget."
#         )

#     else:
#         st.warning(
#             f"You are using your phone {abs(remaining_time):.1f} "
#             "hours above your chosen daily budget."
#         )

#     if current_usage > attention_budget:
#         suggested_reduction = current_usage - attention_budget

#         st.write("### A practical goal")

#         st.write(
#             f"Consider reducing phone use by about "
#             f"{min(suggested_reduction, 0.5):.1f} hour per day "
#             "as a first step, then review your progress."
#         )

#     st.caption(
#         "This budget is a self-selected planning target, not "
#         "a medical guideline. Your total phone use can include "
#         "essential activities such as study, work, and navigation."
#     )

#     # --------------------------------------------------
#     # STEP 5: PERSONALIZED 7-DAY COACH
#     # --------------------------------------------------

#     st.divider()
#     st.header("7-Day Personalized Wellbeing Coach")

#     st.write(
#         "Follow one small, practical habit goal each day. "
#         "Your plan is based on your submitted digital habits."
#     )

#     daily_usage = float(
#         baseline_values["Daily_Usage_Hours"]
#     )
#     sleep_hours = float(
#         baseline_values["Sleep_Hours"]
#     )
#     social_media = float(
#         baseline_values["Time_on_Social_Media"]
#     )
#     gaming_hours = float(
#         baseline_values["Time_on_Gaming"]
#     )
#     bedtime_usage = float(
#         baseline_values["Screen_Time_Before_Bed"]
#     )
#     exercise_hours = float(
#         baseline_values["Exercise_Hours"]
#     )

#     # Build personalized goals from the submitted values.
#     usage_goal = max(0.0, daily_usage - 0.5)
#     social_goal = max(0.0, social_media - 0.5)
#     gaming_goal = max(0.0, gaming_hours - 0.5)

#     if sleep_hours < 8:
#         sleep_goal = min(8.0, sleep_hours + 0.5)
#     else:
#         sleep_goal = sleep_hours

#     bedtime_goal = max(0.0, bedtime_usage - 0.5)

#     exercise_goal = min(8.0, exercise_hours + 0.25)

#     weekly_plan = [
#         {
#             "day": "Day 1",
#             "title": "Understand Your Habits",
#             "goal": (
#                 f"Notice when you use your phone and aim for "
#                 f"no more than {usage_goal:.1f} hours today."
#             )
#         },
#         {
#             "day": "Day 2",
#             "title": "Take a Social Media Break",
#             "goal": (
#                 f"Try keeping social media to "
#                 f"{social_goal:.1f} hours today."
#             )
#         },
#         {
#             "day": "Day 3",
#             "title": "Protect Your Sleep",
#             "goal": (
#                 f"Aim for around {sleep_goal:.1f} hours of sleep "
#                 "and keep your phone away during bedtime."
#             )
#         },
#         {
#             "day": "Day 4",
#             "title": "Create a Screen-Free Wind-Down",
#             "goal": (
#                 f"Reduce screen time before bed to "
#                 f"{bedtime_goal:.1f} hours or less."
#             )
#         },
#         {
#             "day": "Day 5",
#             "title": "Make Time for Offline Activities",
#             "goal": (
#                 f"Try {exercise_goal:.2f} hours of exercise "
#                 "or enjoyable movement, if practical."
#             )
#         },
#         {
#             "day": "Day 6",
#             "title": "Use Gaming Intentionally",
#             "goal": (
#                 f"Plan gaming sessions and aim for "
#                 f"{gaming_goal:.1f} hours or less."
#             )
#         },
#         {
#             "day": "Day 7",
#             "title": "Review and Reflect",
#             "goal": (
#                 "Review which habits felt manageable and choose "
#                 "two goals to continue next week."
#             )
#         }
#     ]

#     for item in weekly_plan:
#         with st.expander(
#             f"{item['day']}: {item['title']}"
#         ):
#             st.write(item["goal"])

#             st.checkbox(
#                 "Mark this day's goal as completed",
#                 key=f"coach_{item['day']}"
#             )

#     completed_days = sum(
#         1
#         for item in weekly_plan
#         if st.session_state.get(
#             f"coach_{item['day']}", False
#         )
#     )

#     st.progress(
#         completed_days / len(weekly_plan),
#         text=f"Weekly goals completed: {completed_days}/7"
#     )

#     st.caption(
#         "This is a self-guided habit plan, not medical advice. "
#         "Goals are suggestions; adjust them to fit your needs."
#     )

#     # --------------------------------------------------
#     # STEP 6: PROGRESS DASHBOARD
#     # --------------------------------------------------

#     st.divider()
#     st.header("Digital Wellbeing Progress Dashboard")

#     st.write(
#         "Review your current habits, model estimates, "
#         "and 7-day coaching progress in one place."
#     )

#     # Key habit metrics
#     col1, col2, col3, col4 = st.columns(4)

#     col1.metric(
#         "Daily Phone Use",
#         f"{baseline_values['Daily_Usage_Hours']:.1f} hrs"
#     )

#     col2.metric(
#         "Sleep",
#         f"{baseline_values['Sleep_Hours']:.1f} hrs"
#     )

#     col3.metric(
#         "Social Media",
#         f"{baseline_values['Time_on_Social_Media']:.1f} hrs"
#     )

#     col4.metric(
#         "Exercise",
#         f"{baseline_values['Exercise_Hours']:.1f} hrs"
#     )

#     # Risk probability chart
#     st.subheader("Current Model Risk Estimates")

#     dashboard_risk = pd.DataFrame({
#         "Risk Category": list(baseline_confidence.keys()),
#         "Probability": list(baseline_confidence.values())
#     }).set_index("Risk Category")

#     st.bar_chart(dashboard_risk)

#     # Compare baseline and adjusted simulator habits
#     st.subheader("Habit Comparison")

#     dashboard_habits = pd.DataFrame({
#         "Original": [
#             baseline_values["Daily_Usage_Hours"],
#             baseline_values["Time_on_Social_Media"],
#             baseline_values["Time_on_Gaming"],
#             baseline_values["Sleep_Hours"],
#             baseline_values["Exercise_Hours"],
#             baseline_values["Screen_Time_Before_Bed"]
#         ],
#         "What-if": [
#             st.session_state.get(
#                 "sim_daily",
#                 baseline_values["Daily_Usage_Hours"]
#             ),
#             st.session_state.get(
#                 "sim_social",
#                 baseline_values["Time_on_Social_Media"]
#             ),
#             st.session_state.get(
#                 "sim_gaming",
#                 baseline_values["Time_on_Gaming"]
#             ),
#             st.session_state.get(
#                 "sim_sleep",
#                 baseline_values["Sleep_Hours"]
#             ),
#             st.session_state.get(
#                 "sim_exercise",
#                 baseline_values["Exercise_Hours"]
#             ),
#             st.session_state.get(
#                 "sim_bed",
#                 baseline_values["Screen_Time_Before_Bed"]
#             )
#         ]
#     }, index=[
#         "Daily phone use",
#         "Social media",
#         "Gaming",
#         "Sleep",
#         "Exercise",
#         "Screen time before bed"
#     ])

#     st.bar_chart(dashboard_habits)

#     # Weekly coach progress
#     st.subheader("7-Day Coach Progress")

#     completed_days = sum(
#         1
#         for day in range(1, 8)
#         if st.session_state.get(
#             f"coach_Day {day}", False
#         )
#     )

#     completion_percentage = completed_days / 7 * 100

#     col1, col2 = st.columns(2)

#     col1.metric(
#         "Completed Goals",
#         f"{completed_days}/7"
#     )

#     col2.metric(
#         "Weekly Completion",
#         f"{completion_percentage:.0f}%"
#     )

#     st.progress(
#         completed_days / 7,
#         text="Your weekly goal completion"
#     )

#     if completed_days == 7:
#         st.success(
#             "Excellent! You completed all seven coaching goals."
#         )
#     elif completed_days > 0:
#         st.info(
#             "Good progress! Keep working toward your remaining goals."
#         )
#     else:
#         st.info(
#             "Start with one small goal today. Progress matters "
#             "more than perfection."
#         )

#     st.caption(
#         "This dashboard reflects the currently submitted profile "
#         "and simulator settings. It does not represent historical "
#         "measurements or prove changes in real-world wellbeing."
#     )


# else:

#     st.info(
#         "Complete the 20-feature form and click "
#         "'Predict My Risk' to view your results and open "
#         "the What-If Habit Simulator."
#     )
    

from pathlib import Path

import joblib
import pandas as pd
import streamlit as st


# --------------------------------------------------
# 1. PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="MindSync AI",
    page_icon="🧠",
    layout="wide"
)



# --------------------------------------------------
# MINDSYNC AI — VISUAL THEME
# --------------------------------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Manrope:wght@400;500;600;700;800&display=swap');

:root {
    --ms-ink: #18243b;
    --ms-muted: #66758d;
    --ms-purple: #7157e8;
    --ms-teal: #28b8a6;
    --ms-border: #e7eaf3;
}
.stApp {
    background:
      radial-gradient(ellipse at 8% 0%, rgba(113,87,232,.10), transparent 34%),
      radial-gradient(ellipse at 95% 12%, rgba(40,184,166,.10), transparent 30%),
      #f7f8fc;
    color: var(--ms-ink);
    font-family: 'DM Sans', sans-serif;
}
[data-testid="stHeader"] { background: rgba(247,248,252,.82); }
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #191b3b 0%, #252955 58%, #253e5b 100%);
    border-right: 1px solid rgba(255,255,255,.08);
}
[data-testid="stSidebar"] * { color: #f7f8ff !important; }
[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p {
    color: #c5cbe6 !important;
}
[data-testid="stSidebar"] [data-testid="stSelectbox"] > div > div {
    background: rgba(255,255,255,.10) !important;
    border: 1px solid rgba(255,255,255,.18) !important;
    border-radius: 10px !important;
}
[data-testid="stSidebar"] div[role="radiogroup"] label {
    background: rgba(255,255,255,.055);
    border: 1px solid rgba(255,255,255,.07);
    border-radius: 12px;
    padding: 10px 12px;
    margin: 5px 0;
    transition: all .2s ease;
}
[data-testid="stSidebar"] div[role="radiogroup"] label:hover {
    background: rgba(255,255,255,.13);
    border-color: rgba(255,255,255,.2);
}
h1, h2, h3 { font-family: 'Manrope', sans-serif !important; color: #202746; letter-spacing: -.035em; }
h1 { font-size: clamp(2rem, 4vw, 3.15rem) !important; font-weight: 800 !important; }
h2 { font-size: 1.65rem !important; font-weight: 800 !important; }
h3 { font-size: 1.15rem !important; font-weight: 750 !important; }
p, label, .stCaption { color: #596780; }
[data-testid="stMetric"] {
    background: linear-gradient(145deg, #fff, #fbfbff);
    border: 1px solid var(--ms-border);
    padding: 18px 20px;
    border-radius: 18px;
    box-shadow: 0 7px 24px rgba(31,42,82,.045);
}
[data-testid="stMetricLabel"] { color: #69758c !important; font-weight: 600; }
[data-testid="stMetricValue"] { color: #24294b !important; font-weight: 800; }
div[data-testid="stForm"], div[data-testid="stExpander"],
div[data-testid="stVerticalBlockBorderWrapper"] {
    border: 1px solid var(--ms-border);
    border-radius: 18px;
    background: rgba(255,255,255,.86);
}
div[data-testid="stForm"] { padding: 24px; box-shadow: 0 10px 35px rgba(31,42,82,.045); }
div[data-testid="stExpander"] { overflow: hidden; }
.stButton > button, .stFormSubmitButton > button {
    border: 0 !important;
    border-radius: 12px !important;
    padding: .72rem 1.1rem !important;
    font-weight: 750 !important;
    transition: transform .18s ease, box-shadow .18s ease !important;
}
.stFormSubmitButton > button, .stButton > button[kind="primary"] {
    background: linear-gradient(100deg, #7157e8, #8a68f0) !important;
    color: white !important;
    box-shadow: 0 8px 20px rgba(113,87,232,.22);
}
.stButton > button:hover, .stFormSubmitButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 12px 25px rgba(113,87,232,.22);
}
input, textarea, [data-baseweb="select"] > div {
    border-radius: 10px !important;
}
.stSlider [data-baseweb="slider"] div[role="slider"] { background: #7157e8; }
.stProgress > div > div > div > div {
    background: linear-gradient(90deg, #7157e8, #31bba8);
}
[data-testid="stAlert"] { border-radius: 14px; border-width: 1px; }
[data-testid="stDataFrame"], [data-testid="stTable"] {
    border: 1px solid var(--ms-border);
    border-radius: 14px;
    overflow: hidden;
}
hr { border-color: #e6e9f2; margin: 2rem 0; }
#MainMenu { visibility: hidden; }
footer { visibility: hidden; }
@media (max-width: 768px) {
    .block-container { padding: 1.1rem 1rem 3rem; }
    div[data-testid="stForm"] { padding: 14px; }
}
</style>
""", unsafe_allow_html=True)



# --------------------------------------------------
# 2. LOAD EXISTING TRAINED MODEL
# --------------------------------------------------

MODEL_PATH = (
    Path(__file__).resolve().parent
    / "mindsync_models"
    / "mindsync_model_bundle.joblib"
)


@st.cache_resource
def load_model_bundle():
    return joblib.load(MODEL_PATH)


if not MODEL_PATH.exists():
    st.error(f"Model bundle not found: {MODEL_PATH}")
    st.info(
        "Check that the mindsync_models folder is "
        "in the same directory as app.py."
    )
    st.stop()

try:
    bundle = load_model_bundle()

    model = bundle["model"]
    scaler = bundle["scaler"]
    FEATURES = bundle["features"]
    CATEGORIES = bundle["categories"]

except Exception as error:
    st.error(f"Could not load model bundle: {error}")
    st.stop()



# --------------------------------------------------
# SIDEBAR BRAND & QUICK NAVIGATION
# --------------------------------------------------
with st.sidebar:
    st.markdown("""
    <div style="padding: 12px 4px 20px;">
      <div style="font-size: 2rem;">🧠</div>
      <div style="font-family:Manrope,sans-serif;font-size:1.45rem;font-weight:800;letter-spacing:-.04em;">MindSync AI</div>
      <div style="font-size:.82rem;color:#c5cbe6;margin-top:4px;">Your space for healthier digital habits</div>
    </div>
    <hr style="border-color:rgba(255,255,255,.15);margin:0 0 16px;">
    """, unsafe_allow_html=True)
    st.markdown("#### Explore MindSync")

    # Highlight the sidebar item matching the section currently in view.
    # Streamlit reruns this app when a sidebar item is selected.
    nav_sections = {
        "Your Profile": "About You",
        "Risk Results": "Your MindSync Results",
        "Habit Simulator": "What-If Habit Simulator",
        "Attention Budget": "Digital Attention Budget",
        "7-Day Coach": "7-Day Personalized Wellbeing Coach",
        "Progress Dashboard": "Digital Wellbeing Progress Dashboard",
    }

    if "active_mindsync_section" not in st.session_state:
        st.session_state.active_mindsync_section = "Your Profile"

    selected_section = st.selectbox(
        "Jump to section",
        list(nav_sections.keys()),
        key="mindsync_section_picker",
        label_visibility="collapsed",
    )
    st.session_state.active_mindsync_section = selected_section

    for nav_label, section_title in nav_sections.items():
        is_active = selected_section == nav_label
        active_style = (
            "background:linear-gradient(90deg,#7865ed,#5c4fc1);"
            "border:1px solid rgba(255,255,255,.24);"
            "box-shadow:0 6px 16px rgba(0,0,0,.16);"
            if is_active else
            "background:rgba(255,255,255,.055);border:1px solid rgba(255,255,255,.07);"
        )
        marker = "●" if is_active else "○"
        st.markdown(
            f'<a href="#{section_title.lower().replace(" ", "-")}" '
            f'style="display:block;text-decoration:none;{active_style}'
            f'border-radius:12px;padding:10px 12px;margin:6px 0;color:#fff;'
            f'font-weight:{"750" if is_active else "500"};">'
            f'<span style="margin-right:9px;">{marker}</span>{nav_label}</a>',
            unsafe_allow_html=True,
        )

    st.markdown("---")
    st.caption("Small steps. Better balance.")


# --------------------------------------------------
# 3. APP HEADER
# --------------------------------------------------

st.markdown("""
<div style="background:linear-gradient(120deg,#24254d 0%,#5146a8 55%,#238e91 100%);
            padding:30px 32px;border-radius:24px;margin:4px 0 22px;
            box-shadow:0 16px 40px rgba(40,43,105,.18);">
  <div style="color:#c9f6ed;font-size:.78rem;font-weight:800;letter-spacing:.14em;text-transform:uppercase;">
    YOUR DIGITAL WELLBEING SPACE
  </div>
  <div style="font-family:Manrope,sans-serif;color:white;font-size:clamp(2rem,4vw,3rem);
              line-height:1.15;font-weight:800;letter-spacing:-.045em;margin:10px 0;">
    MindSync AI <span style="font-size:1.5rem;">✦</span>
  </div>
  <div style="color:#eef0ff;font-size:1.05rem;font-weight:600;">
    Your Personalized Digital Wellbeing and Attention Coach
  </div>
  <div style="color:#d9def7;font-size:.95rem;margin-top:9px;max-width:760px;">
    Understand your habits, explore your digital balance, and take one small step toward a healthier routine.
  </div>
</div>
""", unsafe_allow_html=True)

st.success("Existing trained model loaded successfully.")

with st.expander("Model information"):
    st.write("Model:", type(model).__name__)
    st.write("Required features:", len(FEATURES))
    st.write("Prediction classes:", list(model.classes_))


# --------------------------------------------------
# MINDSYNC AI — OFFLINE RULE-BASED CHATBOT
# No API, no API key, no external AI service
# --------------------------------------------------

def get_chatbot_response(user_question):
    question = user_question.lower().strip()

    # Greetings
    if any(word in question for word in [
        "hello", "hi", "hey", "good morning", "good evening"
    ]):
        return (
            "Hi! Welcome to MindSync AI. 😊\n\n"
            "I can help you understand your digital habits, "
            "risk prediction, habit simulator, attention budget, "
            "and 7-day wellbeing coach. What would you like to know?"
        )

    # About the application
    elif any(word in question for word in [
        "what is mindsync", "about mindsync", "what do you do",
        "purpose of this app", "about this app"
    ]):
        return (
            "**MindSync AI** is a digital wellbeing support tool. "
            "It uses an existing trained machine-learning model "
            "to estimate a risk category from the information "
            "you enter. It also provides habit suggestions, a "
            "What-If Habit Simulator, an attention budget, and "
            "a 7-day self-guided coach."
        )

    # How predictions work
    elif any(word in question for word in [
        "how predict", "how does it work", "how prediction",
        "how model works", "random forest", "machine learning",
        "algorithm", "which model"
    ]):
        return (
            "MindSync uses your submitted profile and digital-habit "
            "values as input to an existing trained Random Forest "
            "model. The app applies the saved scaler, arranges the "
            "20 features in the required order, and predicts a risk "
            "category. The result is a model estimate, not a medical "
            "diagnosis or a guarantee of accuracy."
        )

    # Risk categories
    elif any(word in question for word in [
        "risk level", "risk category", "high risk",
        "medium risk", "low risk", "what does high mean",
        "what does medium mean", "what does low mean"
    ]):
        return (
            "**Risk categories explained:**\n\n"
            "- **High:** The model has placed the submitted profile "
            "in its High category.\n"
            "- **Medium:** The model has placed the profile in its "
            "Medium category.\n"
            "- **Low:** The model has placed the profile in its "
            "Low category.\n\n"
            "These labels reflect the model's learned patterns. "
            "They do not diagnose an addiction or mental-health "
            "condition. Review your habits and use the suggestions "
            "as optional guidance."
        )

    # Probability and confidence
    elif any(word in question for word in [
        "probability", "confidence", "percentage", "score"
    ]):
        return (
            "The probability scores show the model's estimated "
            "probabilities for the available risk categories. "
            "A higher score means the model assigns a higher "
            "probability to that category. These scores should not "
            "be interpreted as a clinical assessment or as a "
            "guarantee that the prediction is correct."
        )

    # Habit simulator
    elif any(word in question for word in [
        "simulator", "what-if", "what if", "change my habits",
        "adjust habits", "before and after"
    ]):
        return (
            "Open the **What-If Habit Simulator** after submitting "
            "your profile. Adjust daily phone use, social media, "
            "gaming, sleep, exercise, or screen time before bed. "
            "MindSync will compare the model's estimates for your "
            "original and adjusted values. This is a hypothetical "
            "comparison, not proof that a habit change causes a "
            "particular result."
        )

    # Attention budget
    elif any(word in question for word in [
        "attention budget", "phone budget", "daily budget",
        "remaining time", "usage limit"
    ]):
        return (
            "The **Digital Attention Budget** lets you choose a "
            "daily phone-use target and compare it with your "
            "submitted daily usage. Try choosing a realistic target "
            "and reducing recreational use gradually. Remember that "
            "total phone use may include essential work, study, "
            "navigation, and communication."
        )

    # 7-day coach
    elif any(word in question for word in [
        "7 day", "7-day", "weekly plan", "coach",
        "daily goal", "complete goals", "wellbeing plan"
    ]):
        return (
            "The **7-Day Personalized Wellbeing Coach** offers "
            "small daily goals related to phone use, social media, "
            "sleep, bedtime screen time, movement, gaming, and "
            "reflection. Expand each day to view its goal and tick "
            "the checkbox when you complete it. The progress bar "
            "shows how many goals you have marked complete."
        )

    # Sleep
    elif any(word in question for word in [
        "sleep", "bedtime", "before bed", "sleeping"
    ]):
        return (
            "A consistent sleep routine can support everyday "
            "wellbeing. You could try keeping your phone away from "
            "your bed, reducing screen use before sleep, and setting "
            "a regular wind-down time. MindSync provides general "
            "habit suggestions, not medical advice."
        )

    # Screen time and phone use
    elif any(word in question for word in [
        "screen time", "phone usage", "phone use",
        "social media", "notifications", "phone checks",
        "reduce mobile", "reduce phone"
    ]):
        return (
            "Start by identifying when and why you use your phone. "
            "You could mute non-essential notifications, set app "
            "timers, take short offline breaks, or plan phone-free "
            "periods during study and bedtime. Choose one manageable "
            "change instead of trying to change everything at once."
        )

    # Personalized suggestions
    elif any(word in question for word in [
        "suggestion", "suggestions", "recommendation",
        "recommendations", "advice", "tips", "improve"
    ]):
        return (
            "Submit your profile using **Predict My Risk** to see "
            "personalized, rule-based suggestions. They may cover "
            "phone use, sleep, bedtime screen time, notifications, "
            "gaming, exercise, and offline social activities. "
            "You can also explore the What-If Simulator and 7-Day "
            "Coach. These suggestions are optional and are not "
            "medical or psychological advice."
        )

    # Data privacy
    elif any(word in question for word in [
        "privacy", "data", "stored", "save my information",
        "personal information"
    ]):
        return (
            "This chatbot processes your question using predefined "
            "rules in this Python app. It does not send your question "
            "to an AI API. The app's other data-handling behaviour "
            "depends on how you deploy and configure Streamlit and "
            "your application. This chatbot alone cannot guarantee "
            "that all application data is never stored."
        )

    # API and AI questions
    elif any(word in question for word in [
        "api", "chatgpt", "generative ai", "real ai",
        "how are you made", "language model"
    ]):
        return (
            "I am MindSync's built-in rule-based assistant. I don't "
            "use an API key, external AI service, or generative "
            "language model. I identify keywords in your question "
            "and return a prepared answer. I can answer supported "
            "MindSync FAQs, but I cannot freely generate answers "
            "to every possible question."
        )

    # Help and available topics
    elif any(word in question for word in [
        "help", "what can i ask", "topics", "options"
    ]):
        return (
            "You can ask me about:\n\n"
            "- MindSync AI and how it works\n"
            "- Risk categories and probability scores\n"
            "- The What-If Habit Simulator\n"
            "- Digital Attention Budget\n"
            "- The 7-Day Wellbeing Coach\n"
            "- Sleep, screen time, and healthy digital habits\n"
            "- How this offline chatbot works\n\n"
            "Try asking: **How does the habit simulator work?**"
        )

    # Fallback for unrecognized questions
    else:
        return (
            "I'm not sure how to answer that yet. I can help with "
            "MindSync AI, risk predictions, digital habits, the "
            "What-If Simulator, Attention Budget, and the 7-Day "
            "Coach.\n\n"
            "Please try asking your question in a different way. "
            "For example: **How can I reduce my screen time?**"
        )


# Chatbot interface
st.divider()

with st.expander("💬 Chat with MindSync AI", expanded=False):
    st.write(
        "Have a question? Ask about your digital habits or "
        "any feature of this application."
    )

    if "mindsync_chat_history" not in st.session_state:
        st.session_state.mindsync_chat_history = [
            {
                "role": "assistant",
                "content": (
                    "Hi! I'm your MindSync helper. Ask me about "
                    "risk predictions, digital habits, the habit "
                    "simulator, or your 7-day coach."
                )
            }
        ]

    # Display previous messages
    for message in st.session_state.mindsync_chat_history:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Input form clears the question after sending
    with st.form("mindsync_chat_form", clear_on_submit=True):
        user_question = st.text_input(
            "Your question",
            placeholder="e.g. How can I reduce my screen time?"
        )

        send_question = st.form_submit_button(
            "Send message",
            type="primary",
            use_container_width=True
        )

    if send_question and user_question.strip():
        answer = get_chatbot_response(user_question)

        st.session_state.mindsync_chat_history.append({
            "role": "user",
            "content": user_question.strip()
        })

        st.session_state.mindsync_chat_history.append({
            "role": "assistant",
            "content": answer
        })

        # Refresh the chat so the new exchange appears immediately
        st.rerun()

    if st.button("Clear chat", key="clear_mindsync_chat"):
        st.session_state.mindsync_chat_history = [
            {
                "role": "assistant",
                "content": "Chat cleared! What would you like to ask?"
            }
        ]
        st.rerun()



# --------------------------------------------------
# 4. PERSONALIZED SUGGESTIONS
# --------------------------------------------------

def get_recommendations(d):
    tips = []

    if d["Daily_Usage_Hours"] >= 6:
        tips.append(
            "Try reducing daily phone use gradually, "
            "starting with 30 minutes less per day."
        )

    if d["Sleep_Hours"] < 7:
        tips.append(
            "Protect your sleep schedule and consider "
            "keeping your phone away from your bed."
        )

    if d["Screen_Time_Before_Bed"] >= 1:
        tips.append(
            "Try a screen-free wind-down period before bedtime."
        )

    if d["Phone_Checks_Per_Day"] >= 80:
        tips.append(
            "Turn off non-essential notifications and check "
            "your phone at planned times."
        )

    if d["Time_on_Social_Media"] >= 3:
        tips.append(
            "Try app timers or planned breaks from social media."
        )

    if d["Time_on_Gaming"] >= 2:
        tips.append(
            "Set planned gaming periods and take regular breaks."
        )

    if d["Apps_Used_Daily"] >= 8:
        tips.append(
            "Review your daily apps and mute notifications "
            "from those that are not important."
        )

    if d["Exercise_Hours"] < 0.5:
        tips.append(
            "Consider adding a short walk or another enjoyable "
            "offline activity to your routine."
        )

    if d["Social_Interactions"] <= 3:
        tips.append(
            "Make time for a conversation or an activity "
            "with friends or family."
        )

    if d["Weekend_Usage_Hours"] >= 7:
        tips.append(
            "Plan one or two offline activities for the weekend."
        )

    if not tips:
        tips.append(
            "Keep maintaining a balance between screen time, "
            "sleep, physical activity, and offline time."
        )

    return tips[:6]


# --------------------------------------------------
# 5. MAIN INPUT FORM: ALL 20 FEATURES
# --------------------------------------------------

with st.form("mindsync_inputs"):

    st.markdown('<div id="about-you"></div>', unsafe_allow_html=True)
    st.header("1. About You")

    col1, col2 = st.columns(2)

    age = col1.number_input(
        "Age",
        min_value=10,
        max_value=100,
        value=24
    )

    gender = col2.selectbox(
        "Gender",
        list(CATEGORIES["Gender"].keys())
    )

    st.header("2. Digital Habits")

    col1, col2 = st.columns(2)

    daily = col1.number_input(
        "Daily phone usage (hours)",
        min_value=0.0,
        max_value=24.0,
        value=5.0,
        step=0.5
    )

    weekend = col2.number_input(
        "Weekend phone usage (hours/day)",
        min_value=0.0,
        max_value=24.0,
        value=6.0,
        step=0.5
    )

    social = col1.number_input(
        "Social media (hours/day)",
        min_value=0.0,
        max_value=24.0,
        value=2.0,
        step=0.5
    )

    gaming = col2.number_input(
        "Gaming (hours/day)",
        min_value=0.0,
        max_value=24.0,
        value=1.0,
        step=0.5
    )

    education = col1.number_input(
        "Educational phone use (hours/day)",
        min_value=0.0,
        max_value=24.0,
        value=1.0,
        step=0.5
    )

    checks = col2.number_input(
        "Phone checks per day",
        min_value=0,
        max_value=1000,
        value=50
    )

    apps = col1.number_input(
        "Apps used daily",
        min_value=0,
        max_value=100,
        value=6
    )

    purpose = col2.selectbox(
        "Main purpose of phone use",
        list(CATEGORIES["Phone_Usage_Purpose"].keys())
    )

    before_bed = col1.number_input(
        "Screen time before bed (hours)",
        min_value=0.0,
        max_value=8.0,
        value=1.0,
        step=0.5
    )

    st.header("3. Lifestyle and Wellbeing")

    col1, col2 = st.columns(2)

    sleep = col1.number_input(
        "Sleep (hours/night)",
        min_value=0.0,
        max_value=14.0,
        value=7.0,
        step=0.5
    )

    exercise = col2.number_input(
        "Exercise (hours/day)",
        min_value=0.0,
        max_value=8.0,
        value=0.5,
        step=0.5
    )

    interactions = col1.slider(
        "Social interactions (0–10)",
        min_value=0,
        max_value=10,
        value=5
    )

    family = col2.slider(
        "Family communication (0–10)",
        min_value=0,
        max_value=10,
        value=5
    )

    academic = col1.slider(
        "Academic performance (0–100)",
        min_value=0,
        max_value=100,
        value=75
    )

    parental = col2.selectbox(
        "Parental controls",
        ["No", "Yes"]
    )

    st.subheader("Additional Model Inputs")

    col1, col2 = st.columns(2)

    anxiety = col1.slider(
        "Anxiety level (0–10)",
        min_value=0,
        max_value=10,
        value=3
    )

    depression = col2.slider(
        "Depression level (0–10)",
        min_value=0,
        max_value=10,
        value=3
    )

    self_esteem = col1.slider(
        "Self-esteem (0–10)",
        min_value=0,
        max_value=10,
        value=7
    )

    submitted = st.form_submit_button(
        "Predict My Risk",
        type="primary",
        use_container_width=True
    )


# --------------------------------------------------
# 6. SAVE THE SUBMITTED BASELINE
# --------------------------------------------------

if "baseline_values" not in st.session_state:
    st.session_state.baseline_values = None


if submitted:

    st.session_state.baseline_values = {
        "Age": age,
        "Gender": CATEGORIES["Gender"][gender],
        "Daily_Usage_Hours": daily,
        "Sleep_Hours": sleep,
        "Academic_Performance": academic,
        "Social_Interactions": interactions,
        "Exercise_Hours": exercise,
        "Anxiety_Level": anxiety,
        "Depression_Level": depression,
        "Self_Esteem": self_esteem,
        "Parental_Control": 1 if parental == "Yes" else 0,
        "Screen_Time_Before_Bed": before_bed,
        "Phone_Checks_Per_Day": checks,
        "Apps_Used_Daily": apps,
        "Time_on_Social_Media": social,
        "Time_on_Gaming": gaming,
        "Time_on_Education": education,
        "Phone_Usage_Purpose": (
            CATEGORIES["Phone_Usage_Purpose"][purpose]
        ),
        "Family_Communication": family,
        "Weekend_Usage_Hours": weekend
    }

    # Reset simulator controls to the newly submitted habits.
    # This is done before the simulator widgets are created.
    st.session_state["sim_daily"] = float(daily)
    st.session_state["sim_social"] = float(social)
    st.session_state["sim_gaming"] = float(gaming)
    st.session_state["sim_sleep"] = float(sleep)
    st.session_state["sim_exercise"] = float(exercise)
    st.session_state["sim_bed"] = float(before_bed)


# --------------------------------------------------
# 7. BASELINE PREDICTION
# --------------------------------------------------

baseline_values = st.session_state.baseline_values


if baseline_values is not None:

    baseline_df = pd.DataFrame(
        [baseline_values]
    )[FEATURES]

    baseline_scaled = scaler.transform(baseline_df)

    baseline_prediction = str(
        model.predict(baseline_scaled)[0]
    )

    baseline_probabilities = model.predict_proba(
        baseline_scaled
    )[0]

    baseline_confidence = dict(
        zip(model.classes_, baseline_probabilities)
    )

    st.divider()
    st.markdown('<div id="your-mindsync-results"></div>', unsafe_allow_html=True)
    st.header("Your MindSync Results")

    if baseline_prediction == "High":
        st.error(
            f"Predicted risk category: {baseline_prediction}"
        )
    elif baseline_prediction == "Medium":
        st.warning(
            f"Predicted risk category: {baseline_prediction}"
        )
    else:
        st.success(
            f"Predicted risk category: {baseline_prediction}"
        )

    st.caption(
        "These probabilities are model estimates, not a medical "
        "diagnosis or a guarantee of prediction accuracy."
    )

    st.subheader("Prediction Probability Scores")

    for label in ["High", "Medium", "Low"]:
        if label in baseline_confidence:
            st.progress(
                float(baseline_confidence[label]),
                text=(
                    f"{label}: "
                    f"{baseline_confidence[label]:.1%}"
                )
            )

    st.subheader("Your Personalized Suggestions")

    for tip in get_recommendations(baseline_values):
        st.markdown(f"- {tip}")

    st.info(
        "MindSync AI provides estimates from your existing trained "
        "model. Suggestions are rule-based and are not medical "
        "or psychological advice."
    )


    # --------------------------------------------------
    # 8. WHAT-IF HABIT SIMULATOR
    # --------------------------------------------------

    st.divider()
    st.markdown('<div id="what-if-habit-simulator"></div>', unsafe_allow_html=True)
    st.header("What-If Habit Simulator")

    st.write(
        "Change selected habits below to explore how the model's "
        "predicted risk category and probability scores may change. "
        "Your original submitted inputs remain unchanged."
    )

    # Initialize simulator controls on their first appearance.
    simulator_defaults = {
        "sim_daily": float(
            baseline_values["Daily_Usage_Hours"]
        ),
        "sim_social": float(
            baseline_values["Time_on_Social_Media"]
        ),
        "sim_gaming": float(
            baseline_values["Time_on_Gaming"]
        ),
        "sim_sleep": float(
            baseline_values["Sleep_Hours"]
        ),
        "sim_exercise": float(
            baseline_values["Exercise_Hours"]
        ),
        "sim_bed": float(
            baseline_values["Screen_Time_Before_Bed"]
        )
    }

    for key, default_value in simulator_defaults.items():
        if key not in st.session_state:
            st.session_state[key] = default_value

    st.subheader("Adjust Your Habits")

    col1, col2 = st.columns(2)

    with col1:

        sim_daily = st.slider(
            "Daily phone usage (hours)",
            min_value=0.0,
            max_value=24.0,
            step=0.5,
            key="sim_daily"
        )

        sim_social = st.slider(
            "Social media (hours/day)",
            min_value=0.0,
            max_value=24.0,
            step=0.5,
            key="sim_social"
        )

        sim_gaming = st.slider(
            "Gaming (hours/day)",
            min_value=0.0,
            max_value=24.0,
            step=0.5,
            key="sim_gaming"
        )

    with col2:

        sim_sleep = st.slider(
            "Sleep (hours/night)",
            min_value=0.0,
            max_value=14.0,
            step=0.5,
            key="sim_sleep"
        )

        sim_exercise = st.slider(
            "Exercise (hours/day)",
            min_value=0.0,
            max_value=8.0,
            step=0.5,
            key="sim_exercise"
        )

        sim_bed = st.slider(
            "Screen time before bed (hours)",
            min_value=0.0,
            max_value=8.0,
            step=0.5,
            key="sim_bed"
        )

    # Start with the saved baseline, not the form's current widgets.
    what_if_values = baseline_values.copy()

    # Change only the six habits selected in the simulator.
    what_if_values["Daily_Usage_Hours"] = sim_daily
    what_if_values["Time_on_Social_Media"] = sim_social
    what_if_values["Time_on_Gaming"] = sim_gaming
    what_if_values["Sleep_Hours"] = sim_sleep
    what_if_values["Exercise_Hours"] = sim_exercise
    what_if_values["Screen_Time_Before_Bed"] = sim_bed

    # Preserve the exact training feature order.
    what_if_df = pd.DataFrame(
        [what_if_values]
    )[FEATURES]

    what_if_scaled = scaler.transform(what_if_df)

    what_if_prediction = str(
        model.predict(what_if_scaled)[0]
    )

    what_if_probabilities = model.predict_proba(
        what_if_scaled
    )[0]

    what_if_confidence = dict(
        zip(model.classes_, what_if_probabilities)
    )

    # --------------------------------------------------
    # 9. COMPARE BASELINE AND WHAT-IF RESULTS
    # --------------------------------------------------

    st.subheader("Before vs. After")

    metric1, metric2 = st.columns(2)

    metric1.metric(
        "Current predicted category",
        baseline_prediction
    )

    metric2.metric(
        "What-if predicted category",
        what_if_prediction
    )

    if baseline_prediction != what_if_prediction:
        st.success(
            f"The predicted category changed from "
            f"{baseline_prediction} to {what_if_prediction}."
        )
    else:
        st.info(
            "The predicted category remains the same for these "
            "adjustments. Check the probability comparison below "
            "for smaller changes in the model's estimates."
        )

    labels = ["High", "Medium", "Low"]

    probability_comparison = pd.DataFrame(
        {
            "Current habits": [
                baseline_confidence.get(label, 0.0)
                for label in labels
            ],
            "What-if habits": [
                what_if_confidence.get(label, 0.0)
                for label in labels
            ]
        },
        index=labels
    )

    st.subheader("Risk Probability Comparison")

    st.bar_chart(probability_comparison)

    display_comparison = probability_comparison.copy()

    display_comparison["Current habits"] = (
        display_comparison["Current habits"].map(
            lambda x: f"{x:.1%}"
        )
    )

    display_comparison["What-if habits"] = (
        display_comparison["What-if habits"].map(
            lambda x: f"{x:.1%}"
        )
    )

    st.dataframe(
        display_comparison,
        use_container_width=True
    )

    # --------------------------------------------------
    # 10. SHOW WHAT CHANGED
    # --------------------------------------------------

    st.subheader("Your Habit Adjustments")

    habit_changes = [
        (
            "Daily phone usage",
            "Daily_Usage_Hours",
            sim_daily,
            "hours/day"
        ),
        (
            "Social media",
            "Time_on_Social_Media",
            sim_social,
            "hours/day"
        ),
        (
            "Gaming",
            "Time_on_Gaming",
            sim_gaming,
            "hours/day"
        ),
        (
            "Sleep",
            "Sleep_Hours",
            sim_sleep,
            "hours/night"
        ),
        (
            "Exercise",
            "Exercise_Hours",
            sim_exercise,
            "hours/day"
        ),
        (
            "Screen time before bed",
            "Screen_Time_Before_Bed",
            sim_bed,
            "hours"
        )
    ]

    changes_found = False

    for name, feature, adjusted_value, unit in habit_changes:

        original_value = float(baseline_values[feature])

        if adjusted_value != original_value:
            changes_found = True

            difference = adjusted_value - original_value

            st.write(
                f"- **{name}:** {original_value:g} → "
                f"{adjusted_value:g} {unit} "
                f"({difference:+g})"
            )

    if not changes_found:
        st.write(
            "No habits have been changed yet. Move a slider "
            "to explore a different scenario."
        )

    st.subheader("Suggestions for Your Adjusted Habits")

    adjusted_tips = get_recommendations(what_if_values)

    for tip in adjusted_tips:
        st.markdown(f"- {tip}")

    st.caption(
        "What-if results are hypothetical model estimates. "
        "They do not prove that changing a habit will cause a "
        "particular outcome. This tool is not a medical assessment."
    )
    
    # --------------------------------------------------
    # STEP 4: DIGITAL ATTENTION BUDGET
    # --------------------------------------------------

    st.divider()
    st.markdown('<div id="digital-attention-budget"></div>', unsafe_allow_html=True)
    st.header("Digital Attention Budget")

    st.write(
        "Set a daily recreational phone-use budget and see "
        "how your current habits compare with your goal."
    )

    attention_budget = st.slider(
        "Your daily recreational phone-use budget (hours)",
        min_value=1.0,
        max_value=12.0,
        value=3.0,
        step=0.5,
        key="attention_budget"
    )

    current_usage = float(
        baseline_values["Daily_Usage_Hours"]
    )

    remaining_time = attention_budget - current_usage

    metric1, metric2, metric3 = st.columns(3)

    metric1.metric(
        "Current daily phone use",
        f"{current_usage:.1f} hours"
    )

    metric2.metric(
        "Your daily budget",
        f"{attention_budget:.1f} hours"
    )

    metric3.metric(
        "Budget remaining",
        f"{max(remaining_time, 0):.1f} hours"
    )

    if remaining_time > 0:
        st.success(
            f"You are {remaining_time:.1f} hours below your "
            "chosen daily budget."
        )

    elif remaining_time == 0:
        st.info(
            "You are exactly at your chosen daily budget."
        )

    else:
        st.warning(
            f"You are using your phone {abs(remaining_time):.1f} "
            "hours above your chosen daily budget."
        )

    if current_usage > attention_budget:
        suggested_reduction = current_usage - attention_budget

        st.write("### A practical goal")

        st.write(
            f"Consider reducing phone use by about "
            f"{min(suggested_reduction, 0.5):.1f} hour per day "
            "as a first step, then review your progress."
        )

    st.caption(
        "This budget is a self-selected planning target, not "
        "a medical guideline. Your total phone use can include "
        "essential activities such as study, work, and navigation."
    )

    # --------------------------------------------------
    # STEP 5: PERSONALIZED 7-DAY COACH
    # --------------------------------------------------

    st.divider()
    st.markdown('<div id="7-day-personalized-wellbeing-coach"></div>', unsafe_allow_html=True)
    st.header("7-Day Personalized Wellbeing Coach")

    st.write(
        "Follow one small, practical habit goal each day. "
        "Your plan is based on your submitted digital habits."
    )

    daily_usage = float(
        baseline_values["Daily_Usage_Hours"]
    )
    sleep_hours = float(
        baseline_values["Sleep_Hours"]
    )
    social_media = float(
        baseline_values["Time_on_Social_Media"]
    )
    gaming_hours = float(
        baseline_values["Time_on_Gaming"]
    )
    bedtime_usage = float(
        baseline_values["Screen_Time_Before_Bed"]
    )
    exercise_hours = float(
        baseline_values["Exercise_Hours"]
    )

    # Build personalized goals from the submitted values.
    usage_goal = max(0.0, daily_usage - 0.5)
    social_goal = max(0.0, social_media - 0.5)
    gaming_goal = max(0.0, gaming_hours - 0.5)

    if sleep_hours < 8:
        sleep_goal = min(8.0, sleep_hours + 0.5)
    else:
        sleep_goal = sleep_hours

    bedtime_goal = max(0.0, bedtime_usage - 0.5)

    exercise_goal = min(8.0, exercise_hours + 0.25)

    weekly_plan = [
        {
            "day": "Day 1",
            "title": "Understand Your Habits",
            "goal": (
                f"Notice when you use your phone and aim for "
                f"no more than {usage_goal:.1f} hours today."
            )
        },
        {
            "day": "Day 2",
            "title": "Take a Social Media Break",
            "goal": (
                f"Try keeping social media to "
                f"{social_goal:.1f} hours today."
            )
        },
        {
            "day": "Day 3",
            "title": "Protect Your Sleep",
            "goal": (
                f"Aim for around {sleep_goal:.1f} hours of sleep "
                "and keep your phone away during bedtime."
            )
        },
        {
            "day": "Day 4",
            "title": "Create a Screen-Free Wind-Down",
            "goal": (
                f"Reduce screen time before bed to "
                f"{bedtime_goal:.1f} hours or less."
            )
        },
        {
            "day": "Day 5",
            "title": "Make Time for Offline Activities",
            "goal": (
                f"Try {exercise_goal:.2f} hours of exercise "
                "or enjoyable movement, if practical."
            )
        },
        {
            "day": "Day 6",
            "title": "Use Gaming Intentionally",
            "goal": (
                f"Plan gaming sessions and aim for "
                f"{gaming_goal:.1f} hours or less."
            )
        },
        {
            "day": "Day 7",
            "title": "Review and Reflect",
            "goal": (
                "Review which habits felt manageable and choose "
                "two goals to continue next week."
            )
        }
    ]

    for item in weekly_plan:
        with st.expander(
            f"{item['day']}: {item['title']}"
        ):
            st.write(item["goal"])

            st.checkbox(
                "Mark this day's goal as completed",
                key=f"coach_{item['day']}"
            )

    completed_days = sum(
        1
        for item in weekly_plan
        if st.session_state.get(
            f"coach_{item['day']}", False
        )
    )

    st.progress(
        completed_days / len(weekly_plan),
        text=f"Weekly goals completed: {completed_days}/7"
    )

    st.caption(
        "This is a self-guided habit plan, not medical advice. "
        "Goals are suggestions; adjust them to fit your needs."
    )

    # --------------------------------------------------
    # STEP 6: PROGRESS DASHBOARD
    # --------------------------------------------------

    st.divider()
    st.markdown('<div id="digital-wellbeing-progress-dashboard"></div>', unsafe_allow_html=True)
    st.header("Digital Wellbeing Progress Dashboard")

    st.write(
        "Review your current habits, model estimates, "
        "and 7-day coaching progress in one place."
    )

    # Key habit metrics
    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Daily Phone Use",
        f"{baseline_values['Daily_Usage_Hours']:.1f} hrs"
    )

    col2.metric(
        "Sleep",
        f"{baseline_values['Sleep_Hours']:.1f} hrs"
    )

    col3.metric(
        "Social Media",
        f"{baseline_values['Time_on_Social_Media']:.1f} hrs"
    )

    col4.metric(
        "Exercise",
        f"{baseline_values['Exercise_Hours']:.1f} hrs"
    )

    # Risk probability chart
    st.subheader("Current Model Risk Estimates")

    dashboard_risk = pd.DataFrame({
        "Risk Category": list(baseline_confidence.keys()),
        "Probability": list(baseline_confidence.values())
    }).set_index("Risk Category")

    st.bar_chart(dashboard_risk)

    # Compare baseline and adjusted simulator habits
    st.subheader("Habit Comparison")

    dashboard_habits = pd.DataFrame({
        "Original": [
            baseline_values["Daily_Usage_Hours"],
            baseline_values["Time_on_Social_Media"],
            baseline_values["Time_on_Gaming"],
            baseline_values["Sleep_Hours"],
            baseline_values["Exercise_Hours"],
            baseline_values["Screen_Time_Before_Bed"]
        ],
        "What-if": [
            st.session_state.get(
                "sim_daily",
                baseline_values["Daily_Usage_Hours"]
            ),
            st.session_state.get(
                "sim_social",
                baseline_values["Time_on_Social_Media"]
            ),
            st.session_state.get(
                "sim_gaming",
                baseline_values["Time_on_Gaming"]
            ),
            st.session_state.get(
                "sim_sleep",
                baseline_values["Sleep_Hours"]
            ),
            st.session_state.get(
                "sim_exercise",
                baseline_values["Exercise_Hours"]
            ),
            st.session_state.get(
                "sim_bed",
                baseline_values["Screen_Time_Before_Bed"]
            )
        ]
    }, index=[
        "Daily phone use",
        "Social media",
        "Gaming",
        "Sleep",
        "Exercise",
        "Screen time before bed"
    ])

    st.bar_chart(dashboard_habits)

    # Weekly coach progress
    st.subheader("7-Day Coach Progress")

    completed_days = sum(
        1
        for day in range(1, 8)
        if st.session_state.get(
            f"coach_Day {day}", False
        )
    )

    completion_percentage = completed_days / 7 * 100

    col1, col2 = st.columns(2)

    col1.metric(
        "Completed Goals",
        f"{completed_days}/7"
    )

    col2.metric(
        "Weekly Completion",
        f"{completion_percentage:.0f}%"
    )

    st.progress(
        completed_days / 7,
        text="Your weekly goal completion"
    )

    if completed_days == 7:
        st.success(
            "Excellent! You completed all seven coaching goals."
        )
    elif completed_days > 0:
        st.info(
            "Good progress! Keep working toward your remaining goals."
        )
    else:
        st.info(
            "Start with one small goal today. Progress matters "
            "more than perfection."
        )

    st.caption(
        "This dashboard reflects the currently submitted profile "
        "and simulator settings. It does not represent historical "
        "measurements or prove changes in real-world wellbeing."
    )


else:

    st.info(
        "Complete the 20-feature form and click "
        "'Predict My Risk' to view your results and open "
        "the What-If Habit Simulator."
    )
    
