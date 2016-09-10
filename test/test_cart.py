import unittest

from shopping.cart import Cart, CannotRemoveFromCart

class MyTestCase(unittest.TestCase):
    def test_theShoppingCartShouldBeEmpty_whenWeCreateANewCart(self):
        cart = Cart()
        self.assertTrue(cart.is_empty())

    def test_theShoppingCartShouldNotBeEmpty_whenWeAddAnItemToTheCart(self):
        cart = Cart()   # Given

        cart.add_item('iPhone')  # When

        self.assertFalse(cart.is_empty())   # Then

    def test_theNumberOfItemsShouldBe0_whenWeCreateANewCart(self):
        cart = Cart()
        self.assertEqual(0, cart.size())

    def test_theNumberOfItemsShouldBe3_whenWeAdd3ItemsToTheCart(self):
        cart = Cart()

        cart.add_item('iPhone')
        cart.add_item('Air Buds')
        cart.add_item('Air Buds')

        self.assertEqual(3, cart.size())

    def test_theNumberOfItemsShouldBeEmpty_whenWeAddAnItemAndThenRemoveIt(self):
        cart = Cart()
        cart.add_item('iPhone')

        cart.remove_item('iPhone')

        self.assertTrue(cart.is_empty())

    def test_itShouldFailBySayingCannotRemoveFromCart_whenWeRemoveItemFromEmptyCart(self):
        cart = Cart()

        with self.assertRaises(CannotRemoveFromCart):
            cart.remove_item('iPhone')

    def test_itShouldFailBySayingCannotRemoveFromCart_whenWeTryToRemoveNonExistantItem(self):
        cart = Cart()

        cart.add_item('iPhone')

        with self.assertRaises(CannotRemoveFromCart):
            cart.remove_item('Air Buds')

    def test_itShouldTellTheQuantityOfSimilarItems_whenItemsAreAddedToTheCart(self):
        cart = Cart()

        cart.add_item('iPhone')
        cart.add_item('iPhone')
        cart.add_item('Air Bud')

        self.assertEqual(2, cart.count_of('iPhone'))

    def test_theItemShouldNotExist_whenItsQuantityIsZero(self):
        cart = Cart()
        cart.add_item('iPhone')
        cart.remove_item('iPhone')

        self.assertEqual(False, cart.exists('iPhone'))

if __name__ == '__main__':
    unittest.main()
