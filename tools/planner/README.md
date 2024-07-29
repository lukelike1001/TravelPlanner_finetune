# **tools/planner** folder 📂

tl;dr Runs sole-planning mode for TravelPlanner using `ReactReflectPlanner` objects, which allow LLMs to reason, act, and reflect using ReAct and Reflexion.

## **Table of Contents: 📖**

### **Python Scripts: 🐍**

- `apis.py`: Stores both the `ReactPlanner` and `ReactReflectPlanner` class for generating travel itineraries. Modify the model here if you'd like to use newer models. For example, you can substitute the default model `gpt-3.5-turbo-1106` for the newly released `gpt-4o-mini`.
- `env.py`: The `run` function is called by `apis.py` whenever the LLM calls the `CostEnquiry[SUBPLAN]` helper function as its action. Modifying the `CostEnquiry[SUBPLAN]` function is key to helping the LLM perform anything from basic arithmetic to generating more insightful reflections.
- `sole_planning.py`: Runs sole-planning model for TravelPlanner. The input prompt contains both the query and supporting information (structured as a JSON object), and generates a JSON output plan (and reflections, if applicable) for an itinerary.

### **Further Reading: 🔎**
Any files and folders not mentioned here have been (nearly) unchanged from the original TravelPlanner found **[here](https://github.com/OSU-NLP-Group/TravelPlanner/tree/90a786d4c5a660aa8ec583dfd40b4d6b058755c8/tools/planner)**.

### **Contact: ☎️**
If you have any questions about any of the files or folders featured here, please reach out to Luke Nam at [lukelike1001@gmail.com](mailto:lukelike1001@gmail.com)
