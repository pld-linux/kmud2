Summary:	kmud - KDE mud client
Summary(pl.UTF-8):	kmud - klient muda dla KDE
Name:		kmud2
Version:	snapshot
Release:	2
License:	GPL
Group:		X11/Applications/Games
Source0:	ftp://ftp.kmud.de/pub/kmud/%{name}-%{version}.tar.gz
# Source0-md5:	11274fdd0a6685ef7df4449610131019
Source1:        http://ep09.pld-linux.org/~djurban/kde/kde-common-admin.tar.bz2
# Source1-md5:	81e0b2f79ef76218381270960ac0f55f
Patch1:		%{name}-makefile-fix.patch
Patch2:		%{name}-const.patch
Patch3:		%{name}-docbook_entity_package.patch
Patch4:		%{name}-desktop.patch
URL:		http://www.kmud.de/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	kdelibs-devel >= 9:3.2.0
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	unsermake >= 040805
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kmud is a graphical MUD client for Linux and other Unix platforms
running KDE. It is a useful and easy-to-use program for all people
that want a nice graphical interface instead of a simple telnet for
playing MUDs. It features a connection wizard/profiles, an automapper,
aliases, triggers (also color triggers, regex support), an input
history (with intelligent browsing), a split screen in the view
history scrollback, numpad walking, speed walking, ANSI/vt100 support
with color customizing, alternative input line and multiline input, a
logging facility, auto login/auto reconnect, a programmable toolbar,
MCCP (mud client compression protocol) support, and a plugin
interface.

%description -l pl.UTF-8
Kmud jest graficznym klientem mudowym dla Linuksa i innych platform
uniksowych używających KDE. Jest to prosty i łatwy w obsłudze program
dla wszystkich ludzi, którzy chcą posiadać ładny, graficzny interfejs
zamiast prostego telneta do grania w mudy. Program ten posiada
'czarodziei' automatycznej i prostej konfiguracji połączeń oraz
profili. Do tego: automapper, aliasy, triggery (także kolorowe - do
podświetlania tekstów), historię komend (wraz z inteligentną
przeglądarką), dzielenie ekranu w oknie przeglądania historii,
chodzenie przy pomocy klawiatury numerycznej, szybkie chodzenie,
wsparcie dla ANSI/vt100 z obsługa ustawień kolorów, alternatywną linię
wpisywania komend oraz wieloliniowe wpisywanie, logowanie,
auto-login/reconnect, programowalny pasek przycisków, MCCP oraz
interfejs wtyczek.

%package devel
Summary:	kmud - development files
Summary(pl.UTF-8):	Pliki programistyczne dla kmuda
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
kmud development files.

%description devel -l pl.UTF-8
Pliki programistyczne dla kmuda.

%prep
%setup -q -n kmud2
rm -rf admin
tar xfj %{SOURCE1}
%patch1 -p0
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
cp -f /usr/share/automake/config.sub admin
# Stupid fellows defined the 'all' target in Makefile.am...
#export UNSERMAKE=/usr/share/unsermake/unsermake
%{__make} -f admin/Makefile.common cvs

%configure \
	--with-qt-libraries=%{_libdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir} \
	kde_libs_htmldir=%{_kdedocdir}

# TODO: add Categories (if not present already)
install -d $RPM_BUILD_ROOT%{_desktopdir}
mv -f $RPM_BUILD_ROOT{%{_datadir}/applnk/Games/*.desktop,%{_desktopdir}}

%find_lang kmud --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f kmud.lang
%defattr(644,root,root,755)
%doc README ChangeLog TODO
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/libkmud.so.*.*.*
%attr(755,root,root) %{_libdir}/kde3/*.so
%{_libdir}/kde3/*.la
%{_datadir}/apps/kmud
%{_datadir}/apps/kmudmapper
%{_iconsdir}/hicolor/*/*/*.png
#%{_iconsdir}/locolor/*/*/*.png
%{_iconsdir}/kmud
%{_datadir}/services/*
%{_datadir}/servicetypes/*
%{_desktopdir}/*.desktop

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libkmud.so
%{_libdir}/libkmud.la
%{_includedir}/kmud
