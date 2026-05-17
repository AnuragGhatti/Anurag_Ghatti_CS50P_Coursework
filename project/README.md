# Finance Tracker

#### Video Demo: <https://youtu.be/dELwPTUUCb4>

#### Description:

My project is a personal finance tracker built in Python. It is designed to help users keep track of their financial activity in a simple and organized way. With this program, users can record both income and expenses, assign categories to each transaction, and view summaries that give them a clearer picture of their overall financial situation.

The main goal of the program is to help users better understand their spending habits over time. Users can continuously add income or expense entries, and all data is stored locally on their device. The program then processes this information to calculate important values such as total income, total expenses, and the user’s net balance. In addition to these totals, it also generates a breakdown of spending by category, which makes it easier to identify where money is being spent the most and where adjustments could be made.

The project is organized into three main files to keep the code clean and easy to manage. The file `project.py` contains the core program logic, including the functions responsible for adding transactions, calculating financial summaries, and generating category-based reports. The file `test_project.py` is used for unit testing and contains tests written using `pytest` to ensure that the main functions behave correctly and produce accurate results. Finally, the `requirements.txt` file lists all necessary dependencies so that the program and tests can be run smoothly in any environment.

For data storage, I chose to use a simple list of dictionaries. This approach keeps the project lightweight and easy to understand while still allowing flexible storage of transaction details such as amount, category, and type. To make sure the data is not lost when the program is closed, I also implemented JSON-based file storage, which allows the information to persist between sessions and be reloaded when the program is started again.

Overall, this project helped me strengthen my understanding of several important Python concepts, including file handling, functions, unit testing, and data organization. It also gave me practical experience in structuring a small application in a way that is modular, readable, and maintainable.

