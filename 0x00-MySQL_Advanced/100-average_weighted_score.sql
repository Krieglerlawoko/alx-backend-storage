-- Create a stored procedure to compute average weighted score for a user
DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
    DECLARE weighted_sum FLOAT;
    DECLARE total_weight INT;

    -- Compute the weighted sum and total weight
    SELECT SUM(c.score * p.weight), SUM(p.weight)
    INTO weighted_sum, total_weight
    FROM corrections c
    JOIN projects p ON c.project_id = p.id
    WHERE c.user_id = user_id;

    -- Update the user's average weighted score
    UPDATE users
    SET average_score = weighted_sum / total_weight
    WHERE id = user_id;
END//

DELIMITER ;
