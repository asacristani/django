# Backend test

## Initial Setup

1. Create a virtualenv with python version 3.11.3 (or another compatible version)
2. Install requirements in the venv by running `pip install -r requirements.txt` at the root of the project
3. Run `python manage.py migrate` to create the database
4. Run `python manage.py setup_data` - this will populate the database with the data needed to run this task


## The project
The app allows users to be invited to the system, and afterwards, to register. We keep track of this wih a simple model `UserMilestone` which links to a User, and a `Milestone` object (either `invitation` or `registration`) and contains a `date` field.

There are a series of available tasks that a user can complete, but only within a given schedule window. This schedule is mapped to both a milestone (i.e. `invitation` or `registration`) and a start offset and end offset field (both stored as duration fields).

Given the above setup, we want to determine which tasks should be available to a user on a given day.

## Tasks

### Task 1

Create a function that calculates the above, and returns a map of users to available tasks.

**For example**:
- A user has an invitation milestone of January 1st 2023
- A task has a schedule with a start offset of 0 and an end offset of 365
- If today is September 20th 2023, the task should be available for that user.

#### Solution
`calculate_available_tasks` function in `user/utils.py`.

Unit testing into `user/tests.py`. You can run them with the following command:
```shell
python manage.py test
```

### Task 2

* Create an API that returns all users for a given task
* Create an API that returns all available tasks for a given user

#### Solution

## Notes

For all of the above, we need to keep performance in mind, and ideally would like to see some form of unit testing being used.
