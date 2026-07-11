%global tl_name mdframed
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.9b
Release:	%{tl_revision}.1
Summary:	Framed environments that can split at page boundaries
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/mdframed
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mdframed.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mdframed.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mdframed.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package develops the facilities of framed in providing breakable
framed and coloured boxes. The user may instruct the package to perform
its operations using default LaTeX commands, PStricks or TikZ.

