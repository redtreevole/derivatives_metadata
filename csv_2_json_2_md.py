#%%
from ast import Assert
import os
import csv
import json

from numpy import var

# %%
def fix_wacky_types(wack_type):
    '''Fixes wacky R dtypes to be more starndard'''

    if wack_type == 'Real':
        return 'float64'
    elif wack_type == 'Integer64':
        return 'Int64'
    elif wack_type == 'Integer':
        return 'Int32'
    else:
        return wack_type


def make_entry_dict(row, headers):
    '''returns a dict for entry'''

    # make dict
    d = {}

    # append fields if non-empty
    for i in range(len(row)):
        if len(row[i]) > 0:
            d[headers[i]] = row[i]

    # fix wacky dtypes
    d['Type'] = fix_wacky_types(d['Type'])

    return(d)


def make_dict_list(file):
    d = []

    with open(file, 'r') as f:
        reader = csv.reader(f)
        for i, entry in enumerate(reader):
            if i == 0:
                # bag the headers
                headers = entry

                # check for mandatory fields
                try:
                    assert ('Variable Name' in headers and 'Description' in headers and 'Type' in headers)
                except AssertionError:
                    raise Exception('Variable Name, Description and Type are required fields.')

            else:
                d.append(make_entry_dict(entry, headers))

    return d


#%%

def make_md_list(dlist):

    # find the keys of all the dicts
    keys = []
    for d in dlist:
        # empty list
        ks = []

        # append keys
        for k in d.keys():
            ks.append(k)

        # add entries of ks to keys
        keys.extend(ks)

    # find unique keys
    keys = list(set(keys))

    # check for mandatory fields
    try:
        assert ('Variable Name' in keys and 'Description' in keys)
    except AssertionError:
        raise Exception('Variable Name and Description are required fields.')

    # order the list so Variabe name and Description come first
    front = ['Variable Name', 'Description']
    front.extend([k for k in keys if k not in front])
    keys = front

    # make headers line
    inside = ' | '.join(keys)
    heads = f'| {inside} |'

    # make divider
    inside = (len(keys) - 2) * '|---'
    divider = f'|---{inside}|---|'

    # put the header and divider into a list
    content = [heads, divider]

    # empty variables list
    variables = []

    # for each dict in dlist...
    for d in dlist:
        # make the string
        s = '| '
        for k in keys:
            try:
                s = s + f'{d[k]} |'
            except KeyError:
                s = s + '   |'

        # append the string to variables
        variables.append(s)

    # put the variables onto the content list
    content.extend(variables)

    return(content)


# %%

# open file
file = '/home/michael/Work/wrtc_derivatives_metadata/crowns.csv'

# make a base filename
base = os.path.basename(file).split('.')[0]

# make dict
dlist = make_dict_list(file)

# dump json
json_path = os.path.join(os.path.dirname(file), f'{base}.json')
with open(json_path, 'w') as j:
    json.dump(dlist, j)

# format markdown file
content = make_md_list(dlist)


md_path = os.path.join(os.path.dirname(file), f'{base}.md')
with open(md_path, 'w') as md:
    md.write('\n')
    for l in content:
        md.write(l + '\n')
# %%

# %%

# %%
