%define fontname andagii

%define fontdir %{_datadir}/fonts/TTF/%{fontname}
%define fontconfdir %{_sysconfdir}/X11/fontpath.d

Summary:	Andagii font for the Osmanya script
Name:		fonts-ttf-%{fontname}
Version:	1.0
Release:	4
License:	GPL
Group:		System/Fonts/True type
Url:		http://www.i18nguy.com/unicode/unicode-font.html
Source0:	%{fontname}.zip
BuildRequires:	fontconfig
BuildRequires:	freetype-tools
BuildArch:	noarch

%description
This package contains the Andagii font for the Osmanya script by
Mark Williamson. Ugaritic and Shavian are also supported.

%files
%dir %{fontdir}
%{fontdir}/*.ttf
%{fontdir}/fonts.*
%{fontconfdir}/*

#----------------------------------------------------------------------------

%prep
%setup -q -c -T
unzip %{SOURCE0}
mv -f ANDAGII_.TTF andagii.ttf

%install
install -m 0755 -d %{buildroot}%{fontdir}
install -m 0644 -p *.ttf %{buildroot}%{fontdir}
ttmkfdir -u %{buildroot}%{fontdir} > %{buildroot}%{fontdir}/fonts.dir
ln -s fonts.dir %{buildroot}%{fontdir}/fonts.scale

install -m 0755 -d %{buildroot}%{fontconfdir}
ln -s ../../../%{fontdir} %{buildroot}%{fontconfdir}/ttf-%{fontname}:pri=50


