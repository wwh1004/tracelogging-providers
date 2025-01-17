import os
import json


def format_obj(obj):
    fmt = 'ProviderNames:\n'

    for provider in obj['ProviderList']:
        fmt += '\t' + provider['ProviderName'] + '\n'

    fmt += '\n\n\n'
    fmt += '**** Events *****\n'

    for event in obj['EventList']:
        fmt += event['EventName']
        fmt += '(\n\t'

        if not event['Fields']:
            fmt += 'VOID'

        i = 0

        for field in event['Fields']:
            i += 1
            if field['OutType']:
                fmt += field['OutType']
            else:
                fmt += field['InType']

            fmt += ' ' + field['FieldName']

            if i != len(event['Fields']):
                fmt += ',\n\t'
        fmt += '\n\t);\n\n'

    return fmt

for filename in os.listdir('.\\Win11_26100\\json'):
    if not filename.endswith('.json'):
        continue

    with open(os.path.join('Win11_26100', 'json', filename), 'r', encoding='utf-8') as f:
        json_obj = json.load(f)

    formatted_obj = format_obj(json_obj)

    with open(os.path.join('Win11_26100', 'tlg', filename.replace('.json', '.tlg')), 'w', encoding='utf-8') as f:
        f.write(formatted_obj)

    print(filename)
