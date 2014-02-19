var lt = require(__dirname + '/../build/Release/node_libtorrent.node');

module.exports = lt;

module.exports.reverse = {
	category_t: {
		0x001: 'error_notification',
		0x002: 'peer_notification',
		0x004: 'port_mapping_notification',
		0x008: 'port_mapping_notification',
		0x010: 'tracker_notification',
		0x020: 'debug_notification',
		0x040: 'status_notification',
		0x080: 'progress_notification',
		0x100: 'ip_block_notification',
		0x200: 'performance_warning',
		0x400: 'dht_notification',
		0x800: 'stats_notification',
	},
	state_t: ['queued_for_checking', 'checking_files', 'downloading_metadata', 'downloading', 'finished', 'seeding', 'allocating', 'checking_resume_data']
};
