-- Create a trigger to update item quantity on new order
DELIMITER //

CREATE TRIGGER update_item_quantity
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    UPDATE items
    SET quantity = quantity - NEW.number
    WHERE name = NEW.item_name;
END//

DELIMITER ;
