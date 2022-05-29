"""Test the task data"""

from collections import namedtuple

Tasks = namedtuple('Task', ['summary', 'owner', 'done', 'id'])
Tasks.__new__.__defaults__ = (None, None, False, None)


def test_asdict():
    """_asdict() should return a dictionary"""
    t_task = Tasks('Do something', 'okken', True, 21)
    t_dict = t_task._asdict()
    expected_data = {
        'summary': 'Do something',
        'owner': 'okken',
        'done': True,
        'id': 21
    }
    assert t_dict == expected_data


def test_replace():
    t_task = Tasks('Do something', 'okken', True, 21)
    t_task = t_task._replace(summary='New summary', done=False)
    t_after = Tasks('New summary', 'okken', False, 21)
    assert t_task == t_after
