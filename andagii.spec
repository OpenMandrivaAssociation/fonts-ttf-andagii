%define fontname andagii

%define fontdir	 %{_datadir}/fonts/TTF/%{fontname}
%define fontconfdir %{_sysconfdir}/X11/fontpath.d

Summary:	 Andagii font for the Osmanya script
Name:		 fonts-ttf-%{fontname}
Version:	 1.0
Release:	 3
Source0:	 %{fontname}.zip
License:	 GPL
Group:		 System/Fonts/True type
Url:		 http://www.i18nguy.com/unicode/unicode-font.html
BuildArch:	 noarch
BuildRequires: fontconfig
BuildRequires:	 freetype-tools

%description
This package contains the Andagii font for the Osmanya script
by Mark Williamson. Ugaritic and Shavian are also supported.

%prep
%setup -q -c -T %{name}-%{version}
unzip %SOURCE0
%__mv -f ANDAGII_.TTF andagii.ttf

%install
%__install -m 0755 -d %{buildroot}%{fontdir}
%__install -m 0644 -p *.ttf %{buildroot}%{fontdir}
ttmkfdir -u %{buildroot}%{fontdir} > %{buildroot}%{fontdir}/fonts.dir
ln -s fonts.dir %{buildroot}%{fontdir}/fonts.scale

%__install -m 0755 -d %{buildroot}%{fontconfdir}
ln -s ../../../%{fontdir} %{buildroot}%{fontconfdir}/ttf-%{fontname}:pri=50

%files
%dir %{fontdir}
%{fontdir}/*.ttf
%{fontdir}/fonts.*
%{fontconfdir}/*


%changelog
* Tue May 17 2011 Funda Wang <fwang@mandriva.org> 1.0-2mdv2011.0
+ Revision: 675515
- br fontconfig for fc-query used in new rpm-setup-build

* Mon Aug 23 2010 Lev Givon <lev@mandriva.org> 1.0-1mdv2011.0
+ Revision: 572490
- import fonts-ttf-andagii


