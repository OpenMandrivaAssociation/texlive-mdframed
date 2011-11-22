# revision 24594
# category Package
# catalog-ctan /macros/latex/contrib/mdframed
# catalog-date 2011-11-14 19:03:15 +0100
# catalog-license lppl
# catalog-version 1.0
Name:		texlive-mdframed
Version:	1.0
Release:	1
Summary:	Framed environments that can split at page boundaries
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/mdframed
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mdframed.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mdframed.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package develops the facilities of framed in providing
breakable framed and coloured boxes.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/mdframed/ltxmdf.cls
%{_texmfdistdir}/tex/latex/mdframed/md-frame-0.mdf
%{_texmfdistdir}/tex/latex/mdframed/md-frame-1.mdf
%{_texmfdistdir}/tex/latex/mdframed/md-frame-2.mdf
%{_texmfdistdir}/tex/latex/mdframed/md-frame-3.mdf
%{_texmfdistdir}/tex/latex/mdframed/mdframed.sty
%doc %{_texmfdistdir}/doc/latex/mdframed/README
%doc %{_texmfdistdir}/doc/latex/mdframed/mdframed-doc-en.pdf
%doc %{_texmfdistdir}/doc/latex/mdframed/mdframed-doc-en.tex
%doc %{_texmfdistdir}/doc/latex/mdframed/mdframed-example-default.pdf
%doc %{_texmfdistdir}/doc/latex/mdframed/mdframed-example-default.tex
%doc %{_texmfdistdir}/doc/latex/mdframed/mdframed-example-pstricks.pdf
%doc %{_texmfdistdir}/doc/latex/mdframed/mdframed-example-pstricks.tex
%doc %{_texmfdistdir}/doc/latex/mdframed/mdframed-example-texsx.pdf
%doc %{_texmfdistdir}/doc/latex/mdframed/mdframed-example-texsx.tex
%doc %{_texmfdistdir}/doc/latex/mdframed/mdframed-example-tikz.pdf
%doc %{_texmfdistdir}/doc/latex/mdframed/mdframed-example-tikz.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
