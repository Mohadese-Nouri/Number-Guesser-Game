# Project: Number Guesser Game

<img src="./images/image1.jpg" width=200>

**Table of contents**<a id='toc0_'></a>       
- [Solutions](#toc1_)
- [How to run](#toc2_)
- [link](#toc3_) 

Welcome to the Number Guesser Game project! This is a fun game that challenges the user to guess a randomly generated number. For each incorrect guess, the user will receive hints to help them, but at the cost of reducing their final score.
## <a id='toc1_'></a>[Solutions](#toc0_)
Inside the `Number Guesser Game Project` directory, you will find three distinct solutions:

1. **Solution A**(single script):
    - **Pros**:
        - Straightforward and simple structure.
        - Easy to understand for beginners.
    - **Cons**:
        - Lacks modularity, making it harder to maintain and expand.
        - All code is lumped together, which can be confusing as the project grows.

2. **Solution B (Using the `src` pattern,Package Structure with `src`)**:
    - **Pros**:
        - Organized with all source code inside the `src` directory.
        - Modular design, separating different functionalities into distinct modules.
        - Includes a `README.md` for detailed explanations and a `requirements.txt` file to manage dependencies.
    - **Cons**:
        - Might be slightly more complex for absolute beginners.
        - Requires understanding of `PYTHONPATH` and Python packaging for optimal execution.
        - **Might be Overkill**: For very small projects or prototypes where rapid development is more crucial than organization, this approach can be excessive. For instance, if you're creating a quick script to automate a mundane task or a one-off data analysis, the overhead of setting up a modular structure might not be justified.
3. **Solution C**(streamlit app):
    - **Pros**:
        - Interactive web-based interface.
        - Easy to deploy and share.
        - Includes a `requirements.txt` file to manage dependencies.
    - **Cons**:
        - Requires understanding of Streamlit and web development.
        - Might be overkill for simple projects.
        - **Requires an Internet Connection**: Streamlit apps run in a web browser, so you need an internet connection to access them. If you're working offline or on a restricted network, this might not be the best solution.

## <a id='toc2_'></a>[How to run](#toc0_)
1. Clone the repository and navigate to the project directory:
    ```bash
    git clone
    cd Number-Guesser-Game-Project
    ```
2. Install the required packages:
    ```bash 
    pip install -r requirements.txt
    ```
3. Run the script:
    ```bash
    python number_guesser.py
    ```



## <a id='toc3_'></a>[Link](#toc0_)
- [Click Here to see the Program in action](https://number-guesser-game-mohadese-nouri.streamlit.app/)
