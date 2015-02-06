Name:           sec
Version:        2.7.6
Release:        2
Summary:        Simple Event Correlator script to filter log file entries
Group:          System/Servers
License:        GPLv2+
URL:            http://simple-evcorr.sourceforge.net/
Source0:        http://downloads.sourceforge.net/simple-evcorr/%{name}-%{version}.tar.gz
Source1:        sec.service
Source3:        sec.logrotate
# Example files and configuration info
Source4:        conf.README
Source5:        http://simple-evcorr.sourceforge.net/rulesets/amavisd.sec
Source6:        http://simple-evcorr.sourceforge.net/rulesets/bsd-MONITOR.sec
Source7:        http://simple-evcorr.sourceforge.net/rulesets/bsd-PHYSMOD.sec
Source8:        http://simple-evcorr.sourceforge.net/rulesets/bsd-USERACT.sec
Source9:        http://simple-evcorr.sourceforge.net/rulesets/bsd-general.sec
Source10:       http://simple-evcorr.sourceforge.net/rulesets/bsd-mpd.sec
Source11:       http://simple-evcorr.sourceforge.net/rulesets/cisco-syslog.sec
Source12:       http://simple-evcorr.sourceforge.net/rulesets/cvs.sec
Source13:       http://simple-evcorr.sourceforge.net/rulesets/dameware.sec
Source14:       http://simple-evcorr.sourceforge.net/rulesets/hp-openview.sec
Source15:       http://simple-evcorr.sourceforge.net/rulesets/labrea.sec
Source16:       http://simple-evcorr.sourceforge.net/rulesets/pix-general.sec
Source17:       http://simple-evcorr.sourceforge.net/rulesets/pix-security.sec
Source18:       http://simple-evcorr.sourceforge.net/rulesets/pix-url.sec
Source19:       http://simple-evcorr.sourceforge.net/rulesets/portscan.sec
Source20:       http://simple-evcorr.sourceforge.net/rulesets/snort.sec
Source21:       http://simple-evcorr.sourceforge.net/rulesets/snortsam.sec
Source22:       http://simple-evcorr.sourceforge.net/rulesets/ssh-brute.sec
Source23:       http://simple-evcorr.sourceforge.net/rulesets/ssh.sec
Source24:       http://simple-evcorr.sourceforge.net/rulesets/vtund.sec
Source25:       http://simple-evcorr.sourceforge.net/rulesets/windows.sec
BuildArch:      noarch

BuildRequires:  systemd

Requires:       logrotate

Requires(post):   systemd
Requires(preun):  systemd
Requires(postun): systemd

%description
SEC is a simple event correlation tool that reads lines from files, named
pipes, or standard input, and matches the lines with regular expressions,
Perl subroutines, and other patterns for recognizing input events.
Events are then correlated according to the rules in configuration files,
producing output events by executing user-specified shell commands, by
writing messages to pipes or files, etc.

%prep
%setup -q

%build

%install
# Install SEC and its associated files
install -D -m 0755 -p sec        %{buildroot}%{_bindir}/sec
install -D -m 0644 -p sec.man    %{buildroot}%{_mandir}/man1/sec.1
install -D -m 0644 -p %{SOURCE1} %{buildroot}%{_unitdir}/sec.service
install -D -m 0644 -p %{SOURCE3} %{buildroot}%{_sysconfdir}/logrotate.d/sec

# Install the example config files and readme
install -D -m 0644 -p %{SOURCE4} %{buildroot}%{_sysconfdir}/%{name}/README
install -d -m 0755  examples
install -m 0644 -p %{SOURCE5} %{SOURCE6} %{SOURCE7} %{SOURCE8} \
                   %{SOURCE9} %{SOURCE10} %{SOURCE11} %{SOURCE12} \
                   %{SOURCE13} %{SOURCE14} %{SOURCE15} %{SOURCE16} \
                   %{SOURCE17} %{SOURCE18} %{SOURCE19} %{SOURCE20} \
                   %{SOURCE21} %{SOURCE22} %{SOURCE23} %{SOURCE24} \
                   %{SOURCE25} examples/

# Remove executable bits because these files get packed as docs
chmod 0644 contrib/convert.pl contrib/swatch2sec.pl

%post
%systemd_post sec.service

%preun
%systemd_preun sec.service

%postun
%systemd_postun_with_restart sec.service

%clean

%files
%defattr(-,root,root,-)
%doc ChangeLog COPYING README contrib/convert.pl contrib/itostream.c contrib/swatch2sec.pl examples
%config(noreplace) %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/logrotate.d/sec
%{_bindir}/sec
%{_mandir}/man1/sec.1*
%{_unitdir}/sec.service

