<?php
error_reporting(0);
if (!file_exists('/tmp/mime.types')) {
file_put_contents("/tmp/mime.types",
fopen("http://svn.apache.org/repos/asf/httpd/httpd/trunk/docs/conf/mime.types",
'r'));
}
$config = array();
$config['db_dsnw'] = 'mysql://' . getenv('DBUSER') . ':' . getenv('DBPASS') .
'@mysql/' . getenv('DBNAME');
$config['default_host'] = 'tls://dovecot';
$config['default_port'] = '143';
$config['smtp_server'] = 'tls://postfix';
$config['smtp_port'] = 587;
$config['smtp_user'] = '%u';
$config['smtp_pass'] = '%p';
$config['support_url'] = '';
$config['product_name'] = 'Roundcube Webmail';
$config['des_key'] = 'yourrandomstring_changeme';
$config['log_dir'] = '/dev/null';
$config['temp_dir'] = '/tmp';
$config['plugins'] = array(
'archive',
'managesieve'
);
$config['skin'] = 'larry';
$config['mime_types'] = '/tmp/mime.types';
$config['imap_conn_options'] = array(
'ssl' => array('verify_peer' => false, 'verify_peer_name' => false,
'allow_self_signed' => true)
);
$config['enable_installer'] = true;
$config['smtp_conn_options'] = array(
'ssl' => array('verify_peer' => false, 'verify_peer_name' => false,
'allow_self_signed' => true)
);
$config['managesieve_port'] = 4190;
$config['managesieve_host'] = 'tls://dovecot';
$config['managesieve_conn_options'] = array(
'ssl' => array('verify_peer' => false, 'verify_peer_name' => false,
'allow_self_signed' => true)
);
// Enables separate management interface for vacation responses (out-of-office)
// 0 - no separate section (default),
// 1 - add Vacation section,
// 2 - add Vacation section, but hide Filters section
$config['managesieve_vacation'] = 1;
