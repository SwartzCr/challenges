import sys
import itertools
import collections

Activity = collections.namedtuple('Activity', 'name calories')
ActivityGroup = collections.namedtuple('ActivityGroup',
                                       'activity_list calorie_total')


def take_input(inp):
    output = []
    lines = inp.readline()
    for i in range(int(lines.strip())):
        output.append(inp.readline().rstrip())
    # FIXME: Crash if there is data left
    return output


def make_lists(lines):
    neg_cal = []
    pos_cal = []
    for line in lines:
        name, calories_str = line.split()
        if calories_str.startswith('-'):
            a = Activity(name=name, calories=int(calories_str))
            neg_cal.append(a)
        else:
            a = Activity(name=name, calories=int(calories_str))
            pos_cal.append(a)
    return (neg_cal, pos_cal)


def make_combinations(activities):
    output = []
    for i in range(len(activities)):
        set_size = i + 1
        output += [x for x in itertools.combinations(activities, set_size)]
    return output


def tabulate(activity_groups):
    output = []
    for entry in activity_groups:
        calorie_total = 0
        activity_list = []
        #if type(entry) == tuple:
        for activity in entry:
                calorie_total += activity.calories
                activity_list.append(activity.name)
        ag = ActivityGroup(activity_list=activity_list,
                           calorie_total=calorie_total)
        output.append(ag)
    return output


def compare(neg_list, pos_list):
    reuslt = False
    for neg_entry in neg_list:
        for pos_entry in pos_list:
            if neg_entry.calorie_total == -(pos_entry.calorie_total):
                result = True
                yield (neg_entry.activity_list,  pos_entry.activity_list)
    if not result:
        yield (['no result'], [])


def write_out(acts):
    for i in range(2):
        for act in acts[i]:
            print act


def main(inp, bool_all):
    list_input = take_input(inp)
    neg_cal_items, pos_cal_items = make_lists(list_input)
    negative_combinations = make_combinations(neg_cal_items)
    positive_combinations = make_combinations(pos_cal_items)
    tabbed_negative_combinations = tabulate(negative_combinations)
    tabbed_positive_combinations = tabulate(positive_combinations)
    if bool_all:
        out_acts = [act for act in compare(tabbed_negative_combinations,
                                           tabbed_positive_combinations)]
    else:
        out_acts = [compare(tabbed_negative_combinations,
                           tabbed_positive_combinations).next()]
    if len(out_acts) < 1:
        write_out((['no result'],[]))
    else:
        for act in out_acts:
            write_out(act)


if __name__ == "__main__":
    if sys.argv[1:2] == ['all']:
        bool_all = True
    else:
        bool_all = False
    main(sys.stdin, bool_all)
