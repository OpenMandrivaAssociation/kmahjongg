#define git 20240217
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
Name:		plasma6-kmahjongg
Summary:	A tile laying patience
Version:	24.05.0
Release:	%{?git:0.%{git}.}1
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
URL:		http://games.kde.org/game.php?game=kmahjongg
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
%if 0%{?git:1}
Source0:	https://invent.kde.org/games/kmahjongg/-/archive/%{gitbranch}/kmahjongg-%{gitbranchd}.tar.bz2#/kmahjongg-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/kmahjongg-%{version}.tar.xz
%endif
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6Svg)
BuildRequires:	cmake(Qt6)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6Crash)
BuildRequires:	cmake(KF6DBusAddons)
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF6Declarative)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(KF6NewStuff)
BuildRequires:	cmake(KF6XmlGui)
BuildRequires:	cmake(KF6)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(KMahjongglib6)
BuildRequires:	cmake(Gettext)
BuildRequires:	cmake(PythonInterp)
BuildRequires:	cmake(KDEGames6)
BuildRequires:	cmake
BuildRequires:	ninja

%description
In KMahjongg the tiles are scrambled and staked on top of each other to
resemble a certain shape. The player is then expected to remove all the
tiles off the game board by locating each tile's matching pair.

%files -f kmahjongg.lang
%{_datadir}/qlogging-categories6/kmahjongg.categories
%{_bindir}/kmahjongg
%{_datadir}/kmahjongg
%{_datadir}/applications/org.kde.kmahjongg.desktop
%{_datadir}/config.kcfg/kmahjongg.kcfg
%{_datadir}/icons/*/*/apps/kmahjongg.*
%{_datadir}/metainfo/org.kde.kmahjongg.appdata.xml

#------------------------------------------------------------------------------

%prep
%autosetup -p1 -n kmahjongg-%{?git:%{gitbranchd}}%{!?git:%{version}}

%build
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja -G Ninja
%ninja

%install
%ninja_install -C build
%find_lang kmahjongg --with-html
