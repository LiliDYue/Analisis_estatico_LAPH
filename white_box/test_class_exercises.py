# -*- coding: utf-8 -*-

"""
White-box unit testing examples.
"""
import unittest

from white_box.class_exercises import (
    DocumentEditingSystem,
    ElevatorSystem,
    TrafficLight,
    UserAuthentication,
    VendingMachine,
    authenticate_user,
    calculate_items_shipping_cost,
    calculate_order_total,
    calculate_quantity_discount,
    calculate_shipping_cost,
    calculate_total_discount,
    categorize_product,
    celsius_to_fahrenheit,
    check_file_size,
    check_flight_eligibility,
    check_loan_eligibility,
    check_number_status,
    divide,
    get_grade,
    get_weather_advisory,
    grade_quiz,
    is_even,
    is_triangle,
    validate_credit_card,
    validate_date,
    validate_email,
    validate_login,
    validate_password,
    validate_url,
    verify_age,
)


class TestWhiteBox(unittest.TestCase):
    """
    White-box unittest class.
    """

    def test_is_even_with_even_number(self):
        """
        Checks if a number is even.
        """
        self.assertTrue(is_even(0))

    def test_is_even_with_odd_number(self):
        """
        Checks if a number is not even.
        """
        self.assertFalse(is_even(7))

    def test_divide_by_non_zero(self):
        """
        Checks the divide function works as expected.
        """
        self.assertEqual(divide(10, 2), 5)

    def test_divide_by_zero(self):
        """
        Checks the divide function returns 0 when dividing by 0.
        """
        self.assertEqual(divide(10, 0), 0)

    def test_get_grade_a(self):
        """
        Checks A grade.
        """
        self.assertEqual(get_grade(95), "A")

    def test_get_grade_b(self):
        """
        Checks B grade.
        """
        self.assertEqual(get_grade(85), "B")

    def test_get_grade_c(self):
        """
        Checks C grade.
        """
        self.assertEqual(get_grade(75), "C")

    def test_get_grade_f(self):
        """
        Checks F grade.
        """
        self.assertEqual(get_grade(65), "F")

    def test_is_triangle_yes(self):
        """
        Checks the three inputs can form a triangle.
        """
        self.assertEqual(is_triangle(3, 4, 5), "Yes, it's a triangle!")

    def test_is_triangle_no_1(self):
        """
        Checks the three inputs can't form a triangle when C is greater or equal than A + B.
        """
        self.assertEqual(is_triangle(3, 4, 7), "No, it's not a triangle.")

    def test_is_triangle_no_2(self):
        """
        Checks the three inputs can't form a triangle when B is greater or equal than A + C.
        """
        self.assertEqual(is_triangle(2, 3, 1), "No, it's not a triangle.")

    def test_is_triangle_no_3(self):
        """
        Checks the three inputs can't form a triangle when A is greater or equal than B + C.
        """
        self.assertEqual(is_triangle(2, 1, 1), "No, it's not a triangle.")


# 1
class TestStatus(unittest.TestCase):
    """
    White-box unittest class for number status
    """

    def test_number_status_whit_positive(self):
        """
        Checks if a given number is positive.
        """

        self.assertEqual(check_number_status(5), "Positive")

    def test_number_status_with_negative(self):
        """
        Checks if a given number is negative.
        """
        self.assertEqual(check_number_status(-4), "Negative")

    def test_number_status_white_zero(self):
        """
        Checks if a given number is zero.
        """
        self.assertEqual(check_number_status(0), "Zero")


# 2
class TestPassword(unittest.TestCase):
    """
    White-box unittest class for validates user passwords.
    """

    def test_validate_password_valida(self):
        """
        Check validate user password
        """
        self.assertTrue(validate_password("aE5!@#$%&"))

    def test_validate_password_length_minor8(self):
        """
        Check the password with length < 8
        """
        self.assertFalse(validate_password("afr"))

    def test_validate_pass_without_uppercase(self):
        """
        Check the password without uppercase
        """
        self.assertFalse(validate_password("afffrw!9"))

    def test_validate_pass_without_lowercase(self):
        """
        Check the password without lowercase
        """
        self.assertFalse(validate_password("AFEOGR!9"))

    def test_validate_pass_without_digits(self):
        """
        Check the password without digits
        """
        self.assertFalse(validate_password("AFEOGR!e"))

    def test_validate_pass_without_specialchar(self):
        """
        Check the password without special character
        """
        self.assertFalse(validate_password("AFEOeRe9"))


# 3
class TestDiscount(unittest.TestCase):
    """
    White-box unittest class for calculate total discount.
    """

    def test_discount_less_than_100(self):
        """
        Check discount when total amount is less than 100
        """
        self.assertEqual(calculate_total_discount(50), 0)

    def test_discount_between_100_and_500(self):
        """
        Check discount when total amount is between 100 and 500
        """
        self.assertEqual(calculate_total_discount(200), 20)

    def test_discount_greater_than_500(self):
        """
        Check discount when total amount is greater than 500
        """
        self.assertEqual(calculate_total_discount(600), 120)


# 4
class TestOrderTotal(unittest.TestCase):
    """
    White-box unittest class for calculate order total.
    """

    def test_quantity_between_1_and_5(self):
        """
        Check total price when quantity is between 1 and 5
        """
        items = [{"quantity": 3, "price": 10}]
        self.assertEqual(calculate_order_total(items), 30)

    def test_quantity_between_6_and_10(self):
        """
        Check total price when quantity is between 6 and 10
        """
        items = [{"quantity": 6, "price": 10}]
        self.assertAlmostEqual(calculate_order_total(items), 57, places=2)

    def test_quantity_greater_than_10(self):
        """
        Check total price when quantity is greater than 10
        """
        items = [{"quantity": 11, "price": 10}]
        self.assertEqual(calculate_order_total(items), 99)


# 5
class TestShippingCost(unittest.TestCase):
    """
    White-box unittest class for calculate items shipping cost.
    """

    def test_standard_shipping_equal_5kg(self):
        """
        Check standard shipping when total weight is equal to 5
        """
        items = [{"weight": 5}]
        self.assertEqual(calculate_items_shipping_cost(items, "standard"), 10)

    def test_standard_shipping_between_5_and_10kg(self):
        """
        Check standard shipping when total weight is between 5 and 10
        """
        items = [{"weight": 7}]
        self.assertEqual(calculate_items_shipping_cost(items, "standard"), 15)

    def test_standard_shipping_greater_10kg(self):
        """
        Check standard shipping when total weight is greater than 10
        """
        items = [{"weight": 15}]
        self.assertEqual(calculate_items_shipping_cost(items, "standard"), 20)

    def test_express_shipping_equal_5kg(self):
        """
        Check express shipping when total weight is equal to 5
        """
        items = [{"weight": 5}]
        self.assertEqual(calculate_items_shipping_cost(items, "express"), 20)

    def test_express_shipping_between_5kg_and_10kg(self):
        """
        Check express shipping when total weight is between to 5 and 10
        """
        items = [{"weight": 8}]
        self.assertEqual(calculate_items_shipping_cost(items, "express"), 30)

    def test_express_shipping_greater_10kg(self):
        """
        Check express shipping when total weight is greater than 10
        """
        items = [{"weight": 15}]
        self.assertEqual(calculate_items_shipping_cost(items, "express"), 40)

    def test_invalid_shipping_method(self):
        """
        Check shipping cost with invalid shipping method
        """
        items = [{"weight": 5}]
        with self.assertRaises(ValueError):
            calculate_items_shipping_cost(items, "invalid")


# 6
class TestLogin(unittest.TestCase):
    """
    White-box unittest class for validate login.
    """

    def test_valid_login(self):
        """
        Check login with valid username and password length
        """
        self.assertEqual(validate_login("usuario1", "password1"), "Login Successful")

    def test_invalid_username_length(self):
        """
        Check login with invalid username length
        """
        self.assertEqual(validate_login("usr", "password1"), "Login Failed")

    def test_invalid_password_length(self):
        """
        Check login with invalid password length
        """
        self.assertEqual(validate_login("usuario1", "pass"), "Login Failed")


# 7
class TestAge(unittest.TestCase):
    """
    White-box unittest class for verify age.
    """

    def test_age_eligible(self):
        """
        Check eligibility when age is between 18 and 65
        """
        self.assertEqual(verify_age(30), "Eligible")

    def test_age_not_eligible(self):
        """
        Check eligibility when age is outside valid range
        """
        self.assertEqual(verify_age(17), "Not Eligible")


# 8
class TestProductCategory(unittest.TestCase):
    """
    White-box unittest class for categorize product.
    """

    def test_category_a(self):
        """
        Check product categorized as Category A
        """
        self.assertEqual(categorize_product(20), "Category A")

    def test_category_b(self):
        """
        Check product categorized as Category B
        """
        self.assertEqual(categorize_product(75), "Category B")

    def test_category_c(self):
        """
        Check product categorized as Category C
        """
        self.assertEqual(categorize_product(150), "Category C")

    def test_category_d(self):
        """
        Check product categorized as Category D
        """
        self.assertEqual(categorize_product(5), "Category D")


# 9
class TestEmail(unittest.TestCase):
    """
    White-box unittest class for validate email.
    """

    def test_valid_email(self):
        """
        Check valid email format
        """
        self.assertEqual(validate_email("test@email.com"), "Valid Email")

    def test_invalid_email(self):
        """
        Check invalid email format
        """
        self.assertEqual(validate_email("testemail.com"), "Invalid Email")


# 10
class TestTemperature(unittest.TestCase):
    """
    White-box unittest class for convert Celsius to Fahrenheit.
    """

    def test_valid_temperature(self):
        """
        Check conversion when temperature is within valid range
        """
        self.assertEqual(celsius_to_fahrenheit(0), 32)

    def test_invalid_temperature(self):
        """
        Check conversion when temperature is outside valid range
        """
        self.assertEqual(celsius_to_fahrenheit(150), "Invalid Temperature")


# 11
class TestCreditCard(unittest.TestCase):
    """
    White-box unittest class for validate credit card.
    """

    def test_valid_card(self):
        """
        Check valid credit card number
        """
        self.assertEqual(validate_credit_card("1234567890123"), "Valid Card")

    def test_invalid_card(self):
        """
        Check invalid credit card number
        """
        self.assertEqual(validate_credit_card("abcd1234"), "Invalid Card")


# 12
class TestDate(unittest.TestCase):
    """
    White-box unittest class for validate date.
    """

    def test_valid_date(self):
        """
        Check valid date values
        """
        self.assertEqual(validate_date(2000, 5, 20), "Valid Date")

    def test_invalid_date(self):
        """
        Check invalid date values
        """
        self.assertEqual(validate_date(1800, 13, 40), "Invalid Date")


# 13
class TestFlightEligibility(unittest.TestCase):
    """
    White-box unittest class for check flight eligibility.
    """

    def test_eligible_by_age(self):
        """
        Check eligibility when age is valid
        """
        self.assertEqual(check_flight_eligibility(30, False), "Eligible to Book")

    def test_eligible_by_frequent_flyer(self):
        """
        Check eligibility when frequent flyer is True
        """
        self.assertEqual(check_flight_eligibility(10, True), "Eligible to Book")

    def test_not_eligible(self):
        """
        Check eligibility when age is invalid and not frequent flyer
        """
        self.assertEqual(check_flight_eligibility(10, False), "Not Eligible to Book")


# 14
class TestURL(unittest.TestCase):
    """
    White-box unittest class for validate URL.
    """

    def test_valid_http_url(self):
        """
        Check valid URL starting with http
        """
        self.assertEqual(validate_url("http://example.com"), "Valid URL")

    def test_invalid_url(self):
        """
        Check invalid URL format
        """
        self.assertEqual(validate_url("ftp://example.com"), "Invalid URL")


# 15
class TestQuantityDiscount(unittest.TestCase):
    """
    White-box unittest class for calculate quantity discount.
    """

    def test_no_discount(self):
        """
        Check when quantity has no discount
        """
        self.assertEqual(calculate_quantity_discount(3), "No Discount")

    def test_5_percent_discount(self):
        """
        Check when quantity gets 5 percent discount
        """
        self.assertEqual(calculate_quantity_discount(7), "5% Discount")

    def test_10_percent_discount(self):
        """
        Check when quantity gets 10 percent discount
        """
        self.assertEqual(calculate_quantity_discount(15), "10% Discount")


# 16
class TestFileSize(unittest.TestCase):
    """
    White-box unittest class for check file size.
    """

    def test_valid_file_size(self):
        """
        Check valid file size
        """
        self.assertEqual(check_file_size(500000), "Valid File Size")

    def test_invalid_file_size(self):
        """
        Check invalid file size
        """
        self.assertEqual(check_file_size(2000000), "Invalid File Size")


# 17
class TestLoanEligibility(unittest.TestCase):
    """
    White-box unittest class for check loan eligibility.
    """

    def test_not_eligible(self):
        """
        Check loan eligibility when income is less than 30000
        """
        self.assertEqual(check_loan_eligibility(20000, 600), "Not Eligible")

    def test_standard_loan(self):
        """
        Check standard loan case
        """
        self.assertEqual(check_loan_eligibility(50000, 750), "Standard Loan")

    def test_premium_loan(self):
        """
        Check premium loan case
        """
        self.assertEqual(check_loan_eligibility(70000, 800), "Premium Loan")


# 18
class TestShippingDimensions(unittest.TestCase):
    """
    White-box unittest class for calculate shipping cost by dimensions.
    """

    def test_small_package(self):
        """
        Check shipping cost for small package
        """
        self.assertEqual(calculate_shipping_cost(1, 10, 10, 10), 5)

    def test_medium_package(self):
        """
        Check shipping cost for medium package
        """
        self.assertEqual(calculate_shipping_cost(3, 20, 20, 20), 10)

    def test_large_package(self):
        """
        Check shipping cost for large package
        """
        self.assertEqual(calculate_shipping_cost(10, 50, 50, 50), 20)


# 19
class TestQuiz(unittest.TestCase):
    """
    White-box unittest class for grade quiz.
    """

    def test_pass(self):
        """
        Check quiz pass condition
        """
        self.assertEqual(grade_quiz(8, 1), "Pass")

    def test_conditional_pass(self):
        """
        Check quiz conditional pass condition
        """
        self.assertEqual(grade_quiz(5, 3), "Conditional Pass")

    def test_fail(self):
        """
        Check quiz fail condition
        """
        self.assertEqual(grade_quiz(3, 5), "Fail")


# 20
class TestAuthenticate(unittest.TestCase):
    """
    White-box unittest class for authenticate user.
    """

    def test_admin_authentication(self):
        """
        Check authentication for admin user
        """
        self.assertEqual(authenticate_user("admin", "admin123"), "Admin")

    def test_normal_user_authentication(self):
        """
        Check authentication for normal user
        """
        self.assertEqual(authenticate_user("usuario", "password1"), "User")

    def test_invalid_authentication(self):
        """
        Check authentication failure
        """
        self.assertEqual(authenticate_user("usr", "pass"), "Invalid")


# 21
class TestWeather(unittest.TestCase):
    """
    White-box unittest class for weather advisory.
    """

    def test_high_temperature_and_humidity(self):
        """
        Check advisory when temperature and humidity are high
        """
        self.assertEqual(
            get_weather_advisory(35, 80),
            "High Temperature and Humidity. Stay Hydrated.",
        )

    def test_low_temperature(self):
        """
        Check advisory when temperature is below zero
        """
        self.assertEqual(get_weather_advisory(-5, 50), "Low Temperature. Bundle Up!")

    def test_no_specific_advisory(self):
        """
        Check advisory when no specific condition is met
        """
        self.assertEqual(get_weather_advisory(20, 50), "No Specific Advisory")


# 22
class TestVendingMachine(unittest.TestCase):
    """
    White-box unittest class for vending machine.
    """

    def setUp(self):
        """
        Creates a new vending machine instance before each test.
        """
        self.vending_machine = VendingMachine()

    def test_vending_machine_initial_state(self):
        """
        Checks the vending machine starts in 'Ready' state.
        """
        self.assertEqual(self.vending_machine.state, "Ready")

    def test_vending_machine_insert_coin_success(self):
        """
        Checks inserting a coin changes state from 'Ready' to 'Dispensing'.
        """
        output = self.vending_machine.insert_coin()

        self.assertEqual(self.vending_machine.state, "Dispensing")
        self.assertEqual(output, "Coin Inserted. Select your drink.")

    def test_vending_machine_insert_coin_error(self):
        """
        Checks inserting a coin in 'Dispensing' state returns an error.
        """
        self.vending_machine.state = "Dispensing"

        output = self.vending_machine.insert_coin()

        self.assertEqual(self.vending_machine.state, "Dispensing")
        self.assertEqual(output, "Invalid operation in current state.")

    def test_vending_machine_select_drink_success(self):
        """
        Checks selecting a drink changes state from 'Dispensing' to 'Ready'.
        """
        self.vending_machine.state = "Dispensing"

        output = self.vending_machine.select_drink()

        self.assertEqual(self.vending_machine.state, "Ready")
        self.assertEqual(output, "Drink Dispensed. Thank you!")

    def test_vending_machine_select_drink_error(self):
        """
        Checks selecting a drink in 'Ready' state returns an error.
        """
        output = self.vending_machine.select_drink()

        self.assertEqual(self.vending_machine.state, "Ready")
        self.assertEqual(output, "Invalid operation in current state.")


# 23
class TestTrafficLight(unittest.TestCase):
    """
    White-box unittest class for traffic light.
    """

    def setUp(self):
        """
        Creates a new traffic light instance before each test.
        """
        self.traffic_light = TrafficLight()

    def test_traffic_light_initial_state(self):
        """
        Checks traffic light starts in 'Red' state.
        """
        self.assertEqual(self.traffic_light.get_current_state(), "Red")

    def test_traffic_light_red_to_green(self):
        """
        Checks state transition from 'Red' to 'Green'.
        """
        self.traffic_light.change_state()

        self.assertEqual(self.traffic_light.get_current_state(), "Green")

    def test_traffic_light_green_to_yellow(self):
        """
        Checks state transition from 'Green' to 'Yellow'.
        """
        self.traffic_light.state = "Green"
        self.traffic_light.change_state()

        self.assertEqual(self.traffic_light.get_current_state(), "Yellow")

    def test_traffic_light_yellow_to_red(self):
        """
        Checks state transition from 'Yellow' to 'Red'.
        """
        self.traffic_light.state = "Yellow"
        self.traffic_light.change_state()

        self.assertEqual(self.traffic_light.get_current_state(), "Red")


# 24
class TestUserAuthentication(unittest.TestCase):
    """
    White-box unittest class for user authentication.
    """

    def setUp(self):
        """
        Creates a new user authentication instance before each test.
        """
        self.user_auth = UserAuthentication()

    def test_user_auth_initial_state(self):
        """
        Checks user starts in 'Logged Out' state.
        """
        self.assertEqual(self.user_auth.state, "Logged Out")

    def test_user_auth_login_success(self):
        """
        Checks login changes state from 'Logged Out' to 'Logged In'.
        """
        output = self.user_auth.login()

        self.assertEqual(self.user_auth.state, "Logged In")
        self.assertEqual(output, "Login successful")

    def test_user_auth_login_error(self):
        """
        Checks login in 'Logged In' state returns an error.
        """
        self.user_auth.state = "Logged In"

        output = self.user_auth.login()

        self.assertEqual(self.user_auth.state, "Logged In")
        self.assertEqual(output, "Invalid operation in current state")

    def test_user_auth_logout_success(self):
        """
        Checks logout changes state from 'Logged In' to 'Logged Out'.
        """
        self.user_auth.state = "Logged In"

        output = self.user_auth.logout()

        self.assertEqual(self.user_auth.state, "Logged Out")
        self.assertEqual(output, "Logout successful")

    def test_user_auth_logout_error(self):
        """
        Checks logout in 'Logged Out' state returns an error.
        """
        output = self.user_auth.logout()

        self.assertEqual(self.user_auth.state, "Logged Out")
        self.assertEqual(output, "Invalid operation in current state")


# 25
class TestDocumentEditingSystem(unittest.TestCase):
    """
    White-box unittest class for document editing system.
    """

    def setUp(self):
        """
        Creates a new document editing system instance before each test.
        """
        self.document_system = DocumentEditingSystem()

    def test_document_initial_state(self):
        """
        Checks document starts in 'Editing' state.
        """
        self.assertEqual(self.document_system.state, "Editing")

    def test_document_save_success(self):
        """
        Checks saving changes state from 'Editing' to 'Saved'.
        """
        output = self.document_system.save_document()

        self.assertEqual(self.document_system.state, "Saved")
        self.assertEqual(output, "Document saved successfully")

    def test_document_save_error(self):
        """
        Checks saving in 'Saved' state returns an error.
        """
        self.document_system.state = "Saved"

        output = self.document_system.save_document()

        self.assertEqual(self.document_system.state, "Saved")
        self.assertEqual(output, "Invalid operation in current state")

    def test_document_edit_success(self):
        """
        Checks editing changes state from 'Saved' to 'Editing'.
        """
        self.document_system.state = "Saved"

        output = self.document_system.edit_document()

        self.assertEqual(self.document_system.state, "Editing")
        self.assertEqual(output, "Editing resumed")

    def test_document_edit_error(self):
        """
        Checks editing in 'Editing' state returns an error.
        """
        output = self.document_system.edit_document()

        self.assertEqual(self.document_system.state, "Editing")
        self.assertEqual(output, "Invalid operation in current state")


# 26
class TestElevatorSystem(unittest.TestCase):
    """
    White-box unittest class for elevator system.
    """

    def setUp(self):
        """
        Creates a new elevator system instance before each test.
        """
        self.elevator_system = ElevatorSystem()

    def test_elevator_initial_state(self):
        """
        Checks elevator starts in 'Idle' state.
        """
        self.assertEqual(self.elevator_system.state, "Idle")

    def test_elevator_move_up_success(self):
        """
        Checks moving up changes state from 'Idle' to 'Moving Up'.
        """
        output = self.elevator_system.move_up()

        self.assertEqual(self.elevator_system.state, "Moving Up")
        self.assertEqual(output, "Elevator moving up")

    def test_elevator_move_down_success(self):
        """
        Checks moving down changes state from 'Idle' to 'Moving Down'.
        """
        output = self.elevator_system.move_down()

        self.assertEqual(self.elevator_system.state, "Moving Down")
        self.assertEqual(output, "Elevator moving down")

    def test_elevator_stop_success_from_up(self):
        """
        Checks stopping changes state from 'Moving Up' to 'Idle'.
        """
        self.elevator_system.move_up()

        output = self.elevator_system.stop()

        self.assertEqual(self.elevator_system.state, "Idle")
        self.assertEqual(output, "Elevator stopped")

    def test_elevator_stop_error(self):
        """
        Checks stopping in 'Idle' state returns an error.
        """
        output = self.elevator_system.stop()

        self.assertEqual(self.elevator_system.state, "Idle")
        self.assertEqual(output, "Invalid operation in current state")
