Name:           sec
Version:        2.5.3
Release:        %mkrel 2
Summary:        Simple Event Correlator
Group:          System/Servers
License:        GPL
URL:            http://www.estpak.ee/~risto/sec/
Source0:        http://prdownloads.sourceforge.net/simple-evcorr/%{name}-%{version}.tar.gz
Source1:        sec.sysconfig
Source2:        sec.init
Source3:        sec.logrotate
Source101:      http://www.estpak.ee/~risto/sec/examples/syslog-ng.txt
Source102:      001_init.sec
Source103:      http://www.bleedingsnort.com/sec/amavisd.sec
Source104:      http://www.bleedingsnort.com/sec/bsd-MONITOR.sec
Source105:      http://www.bleedingsnort.com/sec/bsd-PHYSMOD.sec
Source106:      http://www.bleedingsnort.com/sec/bsd-USERACT.sec
Source107:      http://www.bleedingsnort.com/sec/clamav.sec
Source108:      http://www.bleedingsnort.com/sec/cvs.sec
Source109:      http://www.bleedingsnort.com/sec/dameware.sec
Source110:      http://www.bleedingsnort.com/sec/dbi-example.sec
Source111:      http://www.bleedingsnort.com/sec/general.sec
Source112:      http://www.bleedingsnort.com/sec/hp-openview.sec
Source113:      http://www.bleedingsnort.com/sec/labrea.sec
Source114:      http://www.bleedingsnort.com/sec/mpd.sec
Source115:      http://www.bleedingsnort.com/sec/pix-security.sec
Source116:      http://www.bleedingsnort.com/sec/pix-url.sec
Source117:      http://www.bleedingsnort.com/sec/portscan.sec
Source118:      http://www.bleedingsnort.com/sec/snort.sec
Source119:      http://www.bleedingsnort.com/sec/snortsam.sec
Source120:      http://www.bleedingsnort.com/sec/ssh-brute.sec
Source121:      http://www.bleedingsnort.com/sec/ssh.sec
Source122:      http://www.bleedingsnort.com/sec/vtund.sec
Source123:      http://www.bleedingsnort.com/sec/windows.sec
BuildArch:		noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
SEC is an open source and platform independent event correlation tool that
was designed to fill the gap between commercial event correlation systems and
homegrown solutions that usually comprise a few simple shell scripts.
SEC accepts input from regular files, named pipes, and standard input, and can
thus be employed as an event correlator for any application that is able to
write its output events to a file stream.

%prep
%setup -q

%install
rm -rf %{buildroot}

# Create the directories we'll need
install -d -m 755 %{buildroot}%{_initrddir}
install -d -m 755 %{buildroot}%{_localstatedir}/log
install -d -m 755 %{buildroot}%{_localstatedir}/run
install -d -m 755 %{buildroot}%{_sysconfdir}/logrotate.d
install -d -m 755 %{buildroot}%{_sysconfdir}/sysconfig
install -d -m 755 %{buildroot}%{_sysconfdir}/sec
install -d -m 755 %{buildroot}%{_docdir}/%{name}/examples

# Install SEC and its associated files
install -D -p -m 755 sec.pl     %{buildroot}%{_bindir}/sec
install -D -p -m 644 sec.pl.man %{buildroot}%{_mandir}/man1/sec.1
install -p -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/sysconfig/sec
install -p -m 644 %{SOURCE3} %{buildroot}%{_sysconfdir}/logrotate.d/sec
install -p -m 755 %{SOURCE2} %{buildroot}%{_initrddir}/sec

# Install the example config files
install -m 644 ChangeLog COPYING README \
        %{buildroot}%{_docdir}/%{name}
install -p -m 644 %{SOURCE101} \
        %{buildroot}%{_docdir}/%{name}/examples/syslog-ng.sec
install -p -m 644 %{SOURCE102}  \
                  %{SOURCE103}  \
                  %{SOURCE104}  \
                  %{SOURCE105}  \
                  %{SOURCE106}  \
                  %{SOURCE107}  \
                  %{SOURCE108}  \
                  %{SOURCE109}  \
                  %{SOURCE110}  \
                  %{SOURCE111}  \
                  %{SOURCE112}  \
                  %{SOURCE113}  \
                  %{SOURCE114}  \
                  %{SOURCE115}  \
                  %{SOURCE116}  \
                  %{SOURCE117}  \
                  %{SOURCE118}  \
                  %{SOURCE119}  \
                  %{SOURCE120}  \
                  %{SOURCE121}  \
                  %{SOURCE122}  \
                  %{SOURCE123}  \
        %{buildroot}%{_docdir}/%{name}/examples/

%post
%_post_service %{name}

%preun
%_preun_service %{name}

%clean
rm -rf %{buildroot}

%files

%defattr(-,root,root)
%{_docdir}/%{name}
%config(noreplace) %{_sysconfdir}/sysconfig/sec
%config(noreplace) %{_sysconfdir}/logrotate.d/sec
%{_sysconfdir}/%{name}
%{_bindir}/sec
%{_initrddir}/sec
%{_mandir}/man1/*

