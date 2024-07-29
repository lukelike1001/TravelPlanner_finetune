<h1 align="center">TravelPlanner_finetune<br> Prompt Engineering and Classical Planning Techniques for Improving TravelPlanner Itinerary Generation </h1>

![Travel Planner](https://img.shields.io/badge/Task-Planning-blue)
![Travel Planner](https://img.shields.io/badge/Task-Tool_Use-blue) 
![Travel Planner](https://img.shields.io/badge/Task-Language_Agents-blue)  
![GPT-4](https://img.shields.io/badge/Model-GPT--4-green) 
![LLMs](https://img.shields.io/badge/Model-LLMs-green)

<p align="center">
    <img src="images/icon.png" width="10%"> <br>
</p>

A Branch based on the paper: "[TravelPlanner: A Benchmark for Real-World Planning with Language Agents](http://arxiv.org/abs/2402.01622)".

![Demo Video GIF](images/TravelPlanner.gif)

<p align="center">
[<a href="https://osu-nlp-group.github.io/TravelPlanner/">Website</a>]•
[<a href="http://arxiv.org/abs/2402.01622">Paper</a>] •
[<a href="https://huggingface.co/datasets/osunlp/TravelPlanner">Dataset</a>] •
[<a href="https://huggingface.co/spaces/osunlp/TravelPlannerLeaderboard">Leaderboard</a>] •
[<a href="https://huggingface.co/spaces/osunlp/TravelPlannerEnvironment">Environment</a>] •
[<a href="https://twitter.com/ysu_nlp/status/1754365367294562680">Twitter</a>]
</p>

# TravelPlanner_finetune

TravelPlanner_finetune is a branch of TravelPlanner that strives to improve the base TravelPlanner benchmark using both prompt engineering and classical planning techniques. More specifically, I try to use better formatted prompts to better guide the LLM to reach a valid itinerary, in conjunction with Python helper functions that help the LLM perform basic arithmetic and record keeping.

This repository has only tested prompt engineer and Pythonic function on sole-planning mode, and subfolders featuring changes from the original benchmark contain README files documenting these changes, which you can find here:

## Subfolder README Files
- [`agents/`](agents/README.md): Prompts and algorithms for LLM agents
- [`evaluation/`](evaluation/README.md): Caches output logs and reflections for both raw and modified TravelPlanner runs
- [`selected_database`](selected_database/README.md): Smaller samples of the original TravelPlanner datasets
- [`tools/`](tools/README.md): Tools for searching the travel information CSVs (e.g., accomodations, flights)
- [`tools/planner`](tools/planner/README.md): Tools for running sole-planning mode

## Setup Environment

1. Create a conda environment and install dependency:
```bash
conda create -n travelplanner python=3.9
conda activate travelplanner
pip install -r requirements.txt
```

2. Download the [database](https://drive.google.com/file/d/1pF1Sw6pBmq2sFkJvm-LzJOqrmfWoQgxE/view?usp=drive_link) and unzip it to the `TravelPlanner` directory (i.e., `your/path/TravelPlanner`).

## Running
### Two-stage Mode

Two-stage mode is unchanged from the original TravelPlanner paper, as this branch focuses on the sole-planning mode.

### Sole-Planning Mode

TravelPlanner also provides an easier mode solely focused on testing their planning ability.
The sole-planning mode ensures that no crucial information is missed, thereby enabling agents to focus on planning itself.

Please refer to paper for more details.

```bash
export OUTPUT_DIR=path/to/your/output/file
# We support MODEL in ['gpt-3.5-turbo-X','gpt-4-1106-preview','gemini','mistral-7B-32K','mixtral']
export MODEL_NAME=MODEL_NAME
export OPENAI_API_KEY=YOUR_OPENAI_KEY
# if you do not want to test google models, like gemini, just input "1".
export GOOGLE_API_KEY=YOUR_GOOGLE_KEY
# SET_TYPE in ['validation', 'test']
export SET_TYPE=validation
# STRATEGY in ['direct','cot','react','reflexion']
export STRATEGY=direct

cd tools/planner
python sole_planning.py  --set_type $SET_TYPE --output_dir $OUTPUT_DIR --model_name $MODEL_NAME --strategy $STRATEGY
```

## Postprocess

In order to parse natural language plans, we use gpt-4 to convert these plans into json formats. We encourage developers to try different parsing prompts to obtain better-formatted plans.

```bash
export OUTPUT_DIR=path/to/your/output/file
export MODEL_NAME=MODEL_NAME
export OPENAI_API_KEY=YOUR_OPENAI_KEY
export SET_TYPE=validation
export STRATEGY=direct
# MODE in ['two-stage','sole-planning']
export MODE=two-stage
export TMP_DIR=path/to/tmp/parsed/plan/file
export SUBMISSION_DIR=path/to/your/evaluation/file

cd postprocess
python parsing.py  --set_type $SET_TYPE --output_dir $OUTPUT_DIR --model_name $MODEL_NAME --strategy $STRATEGY --mode $MODE --tmp_dir $TMP_DIR

# Then these parsed plans should be stored as the real json formats.
python element_extraction.py  --set_type $SET_TYPE --output_dir $OUTPUT_DIR --model_name $MODEL_NAME --strategy $STRATEGY --mode $MODE --tmp_dir $TMP_DIR

# Finally, combine these plan files for evaluation. We also provide a evaluation example file "example_evaluation.jsonl" in the postprocess folder.
python combination.py --set_type $SET_TYPE --output_dir $OUTPUT_DIR --model_name $MODEL_NAME --strategy $STRATEGY --mode $MODE  --submission_file_dir $SUBMISSION_DIR
```

## Evaluation

We support the offline validation set evaluation through the provided evaluation script. To avoid data contamination, please use our official [leaderboard](https://huggingface.co/spaces/osunlp/TravelPlannerLeaderboard) for test set evaluation.

```bash
export SET_TYPE=validation
export EVALUATION_FILE_PATH=your/evaluation/file/path

cd evaluation
python eval.py --set_type $SET_TYPE --evaluation_file_path $EVALUATION_FILE_PATH
```

## ⚠️Warnings

The evaluation scripts to foster innovation and aid the development of new methods.  We encourage the use of evaluation feedback in training set, such as implementing reinforcement learning techniques, to enhance learning. However, we strictly prohibit any form of cheating in the validation and test sets to uphold the fairness and reliability of the benchmark's evaluation process. We reserve the right to disqualify results if we find any of the following violations:

1. Reverse engineering of our dataset, which includes, but is not limited to:
   - Converting our natural language queries in the test set to structured formats (e.g., JSON) for optimization and unauthorized evaluation.
   - Deriving data point entries using the hard rules from our data construction process, without accessing the actual database.
   - Other similar manipulations.
2. Hard coding or explicitly writing evaluation cues into prompts by hand, such as direct hints of common sense, which contradicts our goals as it lacks generalizability and is limited to this specific benchmark.
3. Any other human interference strategies that are tailored specifically to this benchmark but lack generalization capabilities.

(The content above is intended solely for use within the TravelPlanner evaluation framework. Extending and editing our database to create new tasks or benchmarks is permitted, provided that you adhere to the licensing terms.)

## Load Datasets

```python
from datasets import load_dataset
# test can be substituted by "train" and "validation".
data = load_dataset('osunlp/TravelPlanner','test')['test']
```

## Contact

If you have any problems with this branch of TravelPlanner, please contact
[Luke Nam](mailto:lukelike1001@gmail.com)

If you have any problems with the original TravelPlanner paper, please contact 
[Jian Xie](mailto:jianx0321@gmail.com),
[Kai Zhang](mailto:zhang.13253@osu.edu),
[Yu Su](mailto:su.809@osu.edu)

## Citation Information

Please cite the original TravelPlanner authors when using their code, paper, or related resources for their research.

<a href="https://github.com/OSU-NLP-Group/TravelPlanner"><img src="https://img.shields.io/github/stars/OSU-NLP-Group/TravelPlanner?style=social&label=TravelPanner" alt="GitHub Stars"></a>

```
@article{xie2024travelplanner,
  title={Travelplanner: A benchmark for real-world planning with language agents},
  author={Xie, Jian and Zhang, Kai and Chen, Jiangjie and Zhu, Tinghui and Lou, Renze and Tian, Yuandong and Xiao, Yanghua and Su, Yu},
  journal={arXiv preprint arXiv:2402.01622},
  year={2024}
}
```
