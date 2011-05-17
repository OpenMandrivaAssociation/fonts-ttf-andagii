%define fontname andagii
%define name	 fonts-ttf-%{fontname}
%define version	 1.0
%define release	 %mkrel 2

%define fontdir	 %{_datadir}/fonts/TTF/%{fontname}
%define fontconfdir %{_sysconfdir}/X11/fontpath.d

Summary:	 Andagii font for the Osmanya script
Name:		 %{name}
Version:	 %{version}
Release:	 %{release}
Source0:	 %{fontname}.zip
License:	 GPL
Group:		 System/Fonts/True type
Url:		 http://www.i18nguy.com/unicode/unicode-font.html
BuildRoot:	 %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	 noarch
BuildRequires: fontconfig
BuildRequires:	 freetype-tools

%description
This package contains the Andagii font for the Osmanya script by Mark Williamson.
Ugaritic and Shavian are also supported.

%prep
%setup -q -c -T %{name}-%{version}
unzip %SOURCE0
%__mv -f ANDAGII_.TTF andagii.ttf

%install
%__rm -rf %{buildroot}

%__install -m 0755 -d %{buildroot}%{fontdir}
%__install -m 0644 -p *.ttf %{buildroot}%{fontdir}
ttmkfdir -u %{buildroot}%{fontdir} > %{buildroot}%{fontdir}/fonts.dir
ln -s fonts.dir %{buildroot}%{fontdir}/fonts.scale

%__install -m 0755 -d %{buildroot}%{fontconfdir}
ln -s ../../../%{fontdir} %{buildroot}%{fontconfdir}/ttf-%{fontname}:pri=50

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%dir %{fontdir}
%{fontdir}/*.ttf
%{fontdir}/fonts.*
%{fontconfdir}/*
