
/****** Number of unique rows  ******/
--SELECT COUNT(DISTINCT id) FROM [AzureTest].[dbo].[invoices];


/****** number of unpaid invoices per organisation  ******/
--SELECT organisation_id, COUNT(*) FROM [AzureTest].[dbo].[invoices] WHERE status LIKE 'UNPAID' GROUP BY organisation_id;


/****** number of overdue invoices per organisation ******/
--SELECT organisation_id, COUNT(*) FROM [AzureTest].[dbo].[invoices] WHERE status LIKE 'UNPAID' AND due_date < GETDATE() GROUP BY organisation_id;


/****** number of paid invoices per month per organisation ******/
--SELECT organisation_id, MONTH(paid_date) as paid_month, COUNT(*) FROM [AzureTest].[dbo].[invoices] WHERE status LIKE 'PAID' GROUP BY organisation_id, MONTH(paid_date) ORDER BY organisation_id;
