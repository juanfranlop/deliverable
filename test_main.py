import unittest
import main
import os

PATH = os.getcwd()

class TestMain(unittest.TestCase):

    def test_is_invalid_batch_int_00(self):
        batch_name = 'batch-00.json'
        full_path_raw_batch_name = os.path.join(PATH, "sample-data", batch_name)
        raw_batch = main.open_raw_batch(full_path_raw_batch_name)
        r1, r2 = main.is_invalid_batch_int(raw_batch)
        result = r1, r2
        self.assertEqual(result, (True, None))

    def test_is_invalid_batch_int_01(self):
        batch_name = 'batch-01.json'
        full_path_raw_batch_name = os.path.join(PATH, "sample-data", batch_name)
        raw_batch = main.open_raw_batch(full_path_raw_batch_name)
        r1, r2 = main.is_invalid_batch_int(raw_batch)
        result = r1, r2
        self.assertEqual(result, (True, None))

    def test_is_invalid_batch_int_02(self):
        batch_name = 'batch-02.json'
        full_path_raw_batch_name = os.path.join(PATH, "sample-data", batch_name)
        raw_batch = main.open_raw_batch(full_path_raw_batch_name)
        r1, r2 = main.is_invalid_batch_int(raw_batch)
        result = r1, r2
        self.assertEqual(result, (True, None))

    def test_is_invalid_batch_int_03(self):
        batch_name = 'batch-03.json'
        full_path_raw_batch_name = os.path.join(PATH, "sample-data", batch_name)
        raw_batch = main.open_raw_batch(full_path_raw_batch_name)
        r1, r2 = main.is_invalid_batch_int(raw_batch)
        result = r1, r2
        self.assertEqual(result, (True, None))

    def test_is_invalid_batch_int_04(self):
        batch_name = 'batch-04.json'
        full_path_raw_batch_name = os.path.join(PATH, "sample-data", batch_name)
        raw_batch = main.open_raw_batch(full_path_raw_batch_name)
        r1, r2 = main.is_invalid_batch_int(raw_batch)
        result = r1, r2
        self.assertEqual(result, (True, None))

    def test_is_invalid_batch_int_05(self):
        batch_name = 'batch-05.json'
        full_path_raw_batch_name = os.path.join(PATH, "sample-data", batch_name)
        raw_batch = main.open_raw_batch(full_path_raw_batch_name)
        r1, r2 = main.is_invalid_batch_int(raw_batch)
        result = r1, r2
        self.assertEqual(result, (True, None))

    def test_is_invalid_batch_int_06(self):
        batch_name = 'batch-06.json'
        full_path_raw_batch_name = os.path.join(PATH, "sample-data", batch_name)
        raw_batch = main.open_raw_batch(full_path_raw_batch_name)
        r1, r2 = main.is_invalid_batch_int(raw_batch)
        result = r1, r2
        self.assertEqual(result, (True, None))

    def test_is_invalid_batch_int_07(self):
        batch_name = 'batch-07.json'
        full_path_raw_batch_name = os.path.join(PATH, "sample-data", batch_name)
        raw_batch = main.open_raw_batch(full_path_raw_batch_name)
        r1, r2 = main.is_invalid_batch_int(raw_batch)
        result = r1, r2
        self.assertEqual(result, (True, None))

    def test_is_invalid_batch_int_08(self):
        batch_name = 'batch-08.json'
        full_path_raw_batch_name = os.path.join(PATH, "sample-data", batch_name)
        raw_batch = main.open_raw_batch(full_path_raw_batch_name)
        r1, r2 = main.is_invalid_batch_int(raw_batch)
        result = r1, r2
        self.assertEqual(result, (True, None))

    def test_is_invalid_batch_int_09(self):
        batch_name = 'batch-09.json'
        full_path_raw_batch_name = os.path.join(PATH, "sample-data", batch_name)
        raw_batch = main.open_raw_batch(full_path_raw_batch_name)
        r1, r2 = main.is_invalid_batch_int(raw_batch)
        result = r1, r2
        self.assertEqual(result, (True, None))

    def test_is_invalid_batch_int_10(self):
        batch_name = 'batch-10.json'
        full_path_raw_batch_name = os.path.join(PATH, "sample-data", batch_name)
        raw_batch = main.open_raw_batch(full_path_raw_batch_name)
        r1, r2 = main.is_invalid_batch_int(raw_batch)
        result = r1, r2
        self.assertEqual(result, (True, None))

    def test_is_invalid_batch_int_11(self):
        batch_name = 'batch-11.json'
        full_path_raw_batch_name = os.path.join(PATH, "sample-data", batch_name)
        raw_batch = main.open_raw_batch(full_path_raw_batch_name)
        r1, r2 = main.is_invalid_batch_int(raw_batch)
        result = r1, r2
        self.assertEqual(result, (True, None))

    def test_is_invalid_batch_int_12(self):
        batch_name = 'batch-12.json'
        full_path_raw_batch_name = os.path.join(PATH, "sample-data", batch_name)
        raw_batch = main.open_raw_batch(full_path_raw_batch_name)
        r1, r2 = main.is_invalid_batch_int(raw_batch)
        result = r1, r2
        self.assertEqual(result, (True, None))

    def test_is_invalid_batch_int_13(self):
        batch_name = 'batch-13.json'
        full_path_raw_batch_name = os.path.join(PATH, "sample-data", batch_name)
        raw_batch = main.open_raw_batch(full_path_raw_batch_name)
        r1, r2 = main.is_invalid_batch_int(raw_batch)
        result = r1, r2
        self.assertEqual(result, (True, None))

    def test_is_invalid_batch_int_14(self):
        batch_name = 'batch-14.json'
        full_path_raw_batch_name = os.path.join(PATH, "sample-data", batch_name)
        raw_batch = main.open_raw_batch(full_path_raw_batch_name)
        r1, r2 = main.is_invalid_batch_int(raw_batch)
        result = r1, r2
        self.assertEqual(result, (False, '11S'))

    def test_is_invalid_batch_int_15(self):
        batch_name = 'batch-15.json'
        full_path_raw_batch_name = os.path.join(PATH, "sample-data", batch_name)
        raw_batch = main.open_raw_batch(full_path_raw_batch_name)
        r1, r2 = main.is_invalid_batch_int(raw_batch)
        result = r1, r2
        self.assertEqual(result, (False, '4T'))

    def test_is_invalid_batch_int_16(self):
        batch_name = 'batch-16.json'
        full_path_raw_batch_name = os.path.join(PATH, "sample-data", batch_name)
        raw_batch = main.open_raw_batch(full_path_raw_batch_name)
        r1, r2 = main.is_invalid_batch_int(raw_batch)
        result = r1, r2
        self.assertEqual(result, (False, '1C'))

    def test_is_invalid_batch_int_17(self):
        batch_name = 'batch-17.json'
        full_path_raw_batch_name = os.path.join(PATH, "sample-data", batch_name)
        raw_batch = main.open_raw_batch(full_path_raw_batch_name)
        r1, r2 = main.is_invalid_batch_int(raw_batch)
        result = r1, r2
        self.assertEqual(result, (False, 'duplicate'))

    def test_is_invalid_batch_int_18(self):
        batch_name = 'batch-18.json'
        full_path_raw_batch_name = os.path.join(PATH, "sample-data", batch_name)
        raw_batch = main.open_raw_batch(full_path_raw_batch_name)
        r1, r2 = main.is_invalid_batch_int(raw_batch)
        result = r1, r2
        self.assertEqual(result, (False, 'incorrect size'))

    def test_is_invalid_batch_int_19(self):
        batch_name = 'batch-19.json'
        full_path_raw_batch_name = os.path.join(PATH, "sample-data", batch_name)
        raw_batch = main.open_raw_batch(full_path_raw_batch_name)
        r1, r2 = main.is_invalid_batch_int(raw_batch)
        result = r1, r2
        self.assertEqual(result, (False, 'incorrect size'))

    ## Test Distance between Data Points

    def test_distance_01(self):
        data_point_1 = main.DataPoint('A', 'H')
        data_point_2 = main.DataPoint('7', 'C')
        self.assertEqual(data_point_1.distance(data_point_2), 18)

    def test_distance_02(self):
        data_point_1 = main.DataPoint('A', 'H')
        data_point_2 = main.DataPoint('A', 'C')
        self.assertEqual(data_point_1.distance(data_point_2), 0)

    def test_distance_03(self):
        data_point_1 = main.DataPoint('A', 'H')
        data_point_2 = main.DataPoint('K', 'H')
        self.assertEqual(data_point_1.distance(data_point_2), 9)

    def test_distance_04(self):
        data_point_1 = main.DataPoint('A', 'H')
        data_point_2 = main.DataPoint('5', 'D')
        self.assertEqual(data_point_1.distance(data_point_2), 8)

    ## Test Data Point Transformation 

    def test_format_batch_01(self):
        raw_batch = ['AH', '5D', 'KH']
        result = [main.DataPoint('A', 'H'), main.DataPoint('5', 'D'), main.DataPoint('K', 'H')]
        self.assertEqual(main.format_batch(raw_batch), result)


if __name__ == '__main__':
    unittest.main()
