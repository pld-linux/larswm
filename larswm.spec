Summary:	Lars Tiling Window Manager
Summary(pl):	Zarz±dca okien larswm
Name:		larswm
Version:	7.2.6
Release:	1
License:	GPL
Group:		X11/Window Managers
Source0:	http://www.fnurt.net/larswm/%{name}-%{version}.tar.gz
URL:		http://www.fnurt.net/larswm/
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Tiling window manager for X, based on David Hogan's 9wm. It provides
virtual desktops, support for tiled and untiled windows, keyboard
shortcuts and more, while using very little system resources. Please
see http://www.fnurt.net/larswm for more information.

%description -l pl
Zarz±dca okien dla X oparty na 9wm. Umo¿liwia korzystanie z
wirtualnych desktopów, "tiled and untiled" okienek, skrótów
klawiszowych i wiele wiêcej przy niewielkim zapotrzebowaniu na zasoby
systemowe. Wiêcej informacji znajduke siê pod adresem
http://www.fnurt.net/larswm/ .

%prep
%setup -q

%build
xmkmf -a
%{__make} CFLAGS="%{rpmcflags}" LDFLAGS="%{rpmldflags}" CC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install install.man \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README README.9wm ChangeLog sample.* *.ms
%attr(0755,root,root) %{_bindir}/*
%{_mandir}/man1/*
