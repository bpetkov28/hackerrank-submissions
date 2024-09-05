SELECT Submissions.hacker_id, Hackers.name FROM Hackers
INNER JOIN Submissions
ON Hackers.hacker_id = Submissions.hacker_id
INNER JOIN Challenges
ON Challenges.challenge_id = Submissions.challenge_id
INNER JOIN Difficulty
ON Challenges.difficulty_level = Difficulty.difficulty_level
WHERE Submissions.score = Difficulty.score
GROUP BY Submissions.hacker_id, Hackers.name
HAVING COUNT(Challenges.challenge_id) > 1
ORDER BY COUNT(Challenges.challenge_id) DESC, Submissions.hacker_id ASC;