import pandas as pd
import numpy as np
from plotly.subplots import make_subplots
import plotly.graph_objects as go

"""=================================================================================================================="""
"""Data Preparation ================================================================================================="""
"""=================================================================================================================="""

coursera_skills_dict = {
    "Operating Systems": 7,
    "Software Engineering": 209,
    "Web Development": 44,
    "Computer Programming": 150,
    "Cloud Computing": 335,
    "Machine Learning": 186,
    "Mathematics": 124,
    "Probability & Statistics": 107,
    "Statistical Programming": 416,
    "Computer Architecture": 45,
}
coursera_skills_data = pd.DataFrame(data=list(coursera_skills_dict.items()),
                                    columns=['Skill', 'Value'])

hackerrank_python_dict = {
    'Introduction':            {'challenges': 6, 'completed': 6},
    'Basic Data Types':        {'challenges': 6, 'completed': 6},
    'Strings':                 {'challenges': 14, 'completed': 14},
    'Sets':                    {'challenges': 13, 'completed': 13},
    'Math':                    {'challenges': 7, 'completed': 7},
    'Itertools':               {'challenges': 7, 'completed': 7},
    'Collections':             {'challenges': 8, 'completed': 8},
    'Date and Time':           {'challenges': 2, 'completed': 2},
    'Classes':                 {'challenges': 2, 'completed': 2},
    'Built-Ins':               {'challenges': 6, 'completed': 6},
    'Python Functions':        {'challenges': 3, 'completed': 3},
    'Regex and Parsing':       {'challenges': 17, 'completed': 17},
    'XML':                     {'challenges': 2, 'completed': 2},
    'Closures and Decorators': {'challenges': 2, 'completed': 2},
    'Numpy':                   {'challenges': 15, 'completed': 15},
    'Debugging':               {'challenges': 2, 'completed': 2},
    }

hackerrank_python_data = pd.DataFrame(data=list(hackerrank_python_dict.items()),
                                      columns=['Skill', 'dict'])

hackerrank_python_data = pd.concat([hackerrank_python_data.drop(['dict'], axis=1),
                                    hackerrank_python_data['dict'].apply(pd.Series)], axis=1)


hackerrank_sql_dict = {
    'Basic Select':            {'challenges': 20, 'completed': 20},
    'Advanced Select':         {'challenges': 5, 'completed': 2},
    'Aggregation':             {'challenges': 17, 'completed': 15},
    'Basic Join':              {'challenges': 8, 'completed': 5},
    'Advanced Join':           {'challenges': 5, 'completed': 1},
    'Alternative Queries':     {'challenges': 3, 'completed': 2},
    }

hackerrank_sql_data = pd.DataFrame(data=list(hackerrank_sql_dict.items()),
                                      columns=['Skill', 'dict',])

hackerrank_sql_data = pd.concat([hackerrank_sql_data.drop(['dict'], axis=1),
                                 hackerrank_sql_data['dict'].apply(pd.Series)], axis=1)

skills_overview = coursera_skills_data.copy()
skills_overview['Value'] = skills_overview['Value'].div(5).round()
additional_skills = {"Data Visualisation": 73,
                     "UI/UX": 40,
                     "SQL": 37,
                     'Operating Systems Adjusted': 34,
                     'Computer Programming Adjusted': 36,
                     'Software Engineering Adjusted': 46,
                     'Cloud Computing Adjusted': 32}


additional_skills_df = pd.DataFrame(np.array(list(additional_skills.items())),
                                    columns=['Skill', 'Value'])

skills_overview = pd.concat([skills_overview,
                             additional_skills_df]).reset_index(drop=True)

skills_overview = skills_overview.sort_values(by=['Skill'])


"""=================================================================================================================="""
"""Data Visualisation ==============================================================================================="""
"""=================================================================================================================="""

fig = make_subplots(
    rows=4, cols=4,
    specs=[[{"colspan": 4}, None, None, None],
           [{"colspan": 2}, None, {"colspan": 2}, None,],
           [{"colspan": 4, 'rowspan': 2}, None, None, None ],
           [None, None, None, None]],
    subplot_titles=(['-' for x in range(6)]),
    )


class vis:
    counter = 0

    @classmethod
    def add_plots(self, x_data, y_data, row, col, plot_type, title):
        fig.add_trace(plot_type(x=x_data,
                                y=y_data,
                                marker=dict(color='navy')),
                      row=row,
                      col=col,)
        fig.layout.annotations[self.counter]['text'] = title
        self.counter += 1
        print('Preparing {} Visualisation - #{}'.format(title, self.counter))
        print()


vis.add_plots(x_data=coursera_skills_data['Skill'],
              y_data=coursera_skills_data['Value'],
              row=1,
              col=1,
              plot_type=go.Bar,
              title="Coursera Beta Skills Distribution")


vis.add_plots(x_data=hackerrank_python_data['Skill'],
              y_data=hackerrank_python_data['completed'] / hackerrank_python_data['challenges'] * 100,
              row=2,
              col=1,
              plot_type=go.Bar,
              title="HackerRank - Python Practice Challenges",)


vis.add_plots(x_data=hackerrank_sql_data['Skill'],
              y_data=hackerrank_sql_data['completed'] / hackerrank_sql_data['challenges'] * 100,
              row=2,
              col=3,
              plot_type=go.Bar,
              title="HackerRank - SQL Practice Challenges")


vis.add_plots(x_data=skills_overview['Skill'],
              y_data=skills_overview['Value'],
              row=3,
              col=1,
              plot_type=go.Bar,
              title="Skills Overview")



fig.update_layout(bargap=0.75,
                  font_family="Times New Roman",
                  font_color="Navy",
                  title_font_family="Times New Roman",
                  title_font_color="Navy",
                  xaxis_title="Skill",
                  yaxis_title="",
                  title="Skills Distribution Visualisation",
                  plot_bgcolor='rgba(0,0,0,0)',

                  )

fig.update_yaxes(showticklabels=True,
                 zeroline=True,
                 showline=True,
                 )

fig.layout.template = 'simple_white'
fig.show()

