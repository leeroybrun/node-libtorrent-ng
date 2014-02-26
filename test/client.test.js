var path = require('path');
var fs = require('fs');
var utils = require('./utils');

var lt = require('..');
var s, th;

var torrentFile = path.join(__dirname, 'files', 'test.torrent');
var tmpDir = path.join(__dirname, 'files', 'tmp');

describe('session', function(){
    before(function() {
        utils.rmdir(tmpDir); // We remove tmp dir before & after, to be sure it's not present when starting or leaving
        fs.mkdirSync(tmpDir);

        s = new lt.session();
        s.listen_on([6881, 6889]);
    });

    after(function() {
        utils.rmdir(tmpDir); // We remove tmp dir before & after, to be sure it's not present when starting or leaving
    });

    describe('add_torrent', function(){
        this.timeout(300000); // Very high timeout for this test suite

        before(function(done) {
            var ti = new lt.torrent_info(torrentFile);
            th = s.add_torrent({
                ti: ti,
                save_path: tmpDir
            });

            setTimeout(function() {
                st = th.status();
                done();
            }, 180000);
        });

        it('should not be errored', function(){
            st.error.should.have.length(0);
        });
        it('should have progressed', function(){
            st.progress.should.be.above(0);
        });
    })
});
