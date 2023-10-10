import csv

# from app import db
from app.models.racquet import Racquet, RacquetSchema
from app.models.pattern_type import PatternType, PatternTypeSchema
from app.models.manufacturer import Manufacturer, ManufacturerSchema


def get_or_create_manufacturer(name):
    manufacturer = Manufacturer.get_one_by_name(name)

    if manufacturer:
        return manufacturer.id
    else:
        try:
            manufacturer_data = ManufacturerSchema.load({'name': name})
            manufacturer = Manufacturer(manufacturer_data)
            # manufacturer.save()
            print(manufacturer)

            return manufacturer.id
        except Exception as err:
            print("Failed to create manufacturer: {}, with error: {}".format(name, err))
            # logging.exception(err)
            # db.session.rollback()


def get_or_create_pattern_type(name):
    pattern_type = PatternType.get_one_by_name(name)

    if pattern_type:
        return pattern_type.id
    else:
        try:
            pattern_type_data = PatternTypeSchema.load({'pattern_type': name})
            pattern_type = PatternType(pattern_type_data)
            # pattern_type.save()
            print(pattern_type)

            return pattern_type.id
        except Exception as err:
            print("Failed to create pattern_type: {}, with error: {}".format(name, err))
            # logging.exception(err)
            # db.session.rollback()


# # name varchar
# # headsize int
# # num_crosses int
# # num_crosses int
# # num_mains int
# # manufacturer_id int [ref: > M.id]
# # len_crosses varchar
# # len_mains varchar
# # start_cross varchar
# # start_main varchar
# # tie_cross varchar
# # tie_main varchar
# # skip_cross varchar
# # skip_main varchar
# # short_side varchar
# # long_side varchar
# # url url
# # url = fields.Url()


def create_racquet(data):
    try:
        racquet_data = RacquetSchema.load(data)
        racquet = Racquet(racquet_data)
        # racquet.save()
        print(racquet)
    except Exception as err:
        print("Failed to create racquet with data: {}, error: {}".format(data, err))
        # logging.exception(err)
        # db.session.rollback()




def import_racquets():
    with open('data.csv', newline='') as csvfile:
        # Format of data .csv
        # 0 Racquet Name
        # 1 Tension
        # 2 Length
        # 3 Pattern
        # 4 Skip M Holes
        # 5 Tie Off M
        # 6 Start C
        # 7 Tie Off C
        # 8 Manufacturer
        # 9 Pattern Type

        data = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in data:
            import_data = {
                'name': row[0],
                # 'headsize': '',  # row 2
                'num_crosses': row[3].split(' X ')[1],  # row 3
                'num_mains': row[3].split(' X ')[0],  # row 3
                'manufacturer_id': get_or_create_manufacturer(row[8]),  # row 8
                'len_crosses': row[2].split(' - ')[1],  # row 2
                'len_mains': row[2].split(' - ')[0],  # row 2
                'start_cross': row[6],  # row 6
                # 'start_main': '',  # row 2
                'tie_cross': row[7],  # row 7
                'tie_main': row[5],  # row 5
                'skip_cross': row[6],  # row 4
                'skip_main': row[4],  # row 4
                'short_side': row[4],  # row 2
                'long_side': row[4],  # row 2
                'pattern_type_id': get_or_create_pattern_type(row[9])  # row 9
                # tension_high: ''  # row 1
                # tension_low : ''  # row 1
            }

            create_racquet(import_data)


import_racquets()
