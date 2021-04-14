SET FOREIGN_KEY_CHECKS = 0;
insert into account_school value(1, '乐山职业技术学院', 'ASDFASF');
insert into interest_interestorganization value(1,'Python兴趣爱好者', 'python学习聚集地，欢迎大佬们常驻', 'o', 1);
insert into interest_tag value(1, 'python');
insert into interest_article value(1, 'python学习路线', 'python学习路线python学习路线python学习路线python学习路线python学习路线python学习路线', 'o', 20, 5, 'o', 1);
insert into interest_article_tags value (1, 1, 1);
SET FOREIGN_KEY_CHECKS = 1;