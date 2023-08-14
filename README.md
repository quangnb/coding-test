# coding-test
API description: 
self.api.get_field_size() -> int
Returns the width and height of the field. The field is always square, and the minimum size is 1.

self.api.get_number_of_cows() -> int
Returns the total number of cows grazing the field.

self.api.get_x_coordinate_for_cow(cow_index: int) -> int
Returns the X-coordinate for the given cow index. Starting at index 0 and limited by the total number of cows.

self.api.get_y_coordinate_for_cow(cow_index: int) -> int
Returns the Y-coordinate for the given cow index. Starting at index 0 and limited by the total number of cows.
