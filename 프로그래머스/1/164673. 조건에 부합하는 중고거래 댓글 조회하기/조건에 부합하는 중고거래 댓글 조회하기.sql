SELECT 
    b.TITLE AS TITLE,
    b.BOARD_ID AS BOARD_ID,
    r.REPLY_ID AS REPLY_ID,
    r.WRITER_ID AS WRITER_ID,
    r.CONTENTS AS CONTENTS,
    DATE_FORMAT(r.CREATED_DATE, '%Y-%m-%d') AS CREATED_DATE
FROM 
    USED_GOODS_BOARD b
JOIN 
    USED_GOODS_REPLY r ON b.BOARD_ID = r.BOARD_ID
WHERE 
    b.CREATED_DATE >= '2022-10-01' AND b.CREATED_DATE < '2022-11-01'
    AND r.CREATED_DATE >= '2022-10-01' AND r.CREATED_DATE < '2022-11-01'
;

SELECT a.title, b.BOARD_ID, b.reply_id, b.writer_id, b.contents, 
date_format(b.created_date,'%Y-%m-%d')as Created_date
from USED_GOODS_board as a
inner join USED_GOODS_reply as b 
on a.board_id = b.board_id
where a.created_date between '2022-10-01' and '2022-10-30'
order by b.created_date asc, a.title asc;