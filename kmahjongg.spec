Name:		kmahjongg
Summary:	A tile laying patience
Version:	17.03.80
Release:	1
Epoch:		1
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
URL:		http://games.kde.org/game.php?game=kmahjongg
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
Source0:	http://download.kde.org/%{stable}/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5Svg)
BuildRequires:	cmake(Qt5)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5Crash)
BuildRequires:	cmake(KF5DBusAddons)
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5Declarative)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(KF5NewStuff)
BuildRequires:	cmake(KF5XmlGui)
BuildRequires:	cmake(KF5)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(KF5KMahjongglib)
BuildRequires:	cmake(Gettext)
BuildRequires:	cmake(PythonInterp)
BuildRequires:	cmake(KF5KDEGames)
BuildRequires:	cmake
BuildRequires:	ninja

%description
In KMahjongg the tiles are scrambled and staked on top of each other to
resemble a certain shape. The player is then expected to remove all the
tiles off the game board by locating each tile's matching pair.

%files
%{_bindir}/kmahjongg
%{_datadir}/kmahjongg
%{_datadir}/kxmlgui5/kmahjongg
%{_datadir}/applications/org.kde.kmahjongg.desktop
%{_datadir}/config.kcfg/kmahjongg.kcfg
%doc %{_docdir}/HTML/en/kmahjongg
%{_datadir}/icons/*/*/apps/kmahjongg.*


#------------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde5 -G Ninja
%ninja

%install
%ninja_install -C build
