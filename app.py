import streamlit as st
import joblib
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')

# ═══════════════════════════════════════
# إعدادات الصفحة
# ═══════════════════════════════════════
st.set_page_config(
    page_title="DiscourSense — ANNODIS",
    page_icon="🧠",
    layout="wide"
)

# ═══════════════════════════════════════
# CSS مخصص
# ═══════════════════════════════════════
st.markdown("""
<style>
/* الخط العام */
html, body, [class*="css"] {
    font-family: 'Segoe UI', sans-serif;
}

/* العنوان الرئيسي */
.main-title {
    font-size: 2.2rem;
    font-weight: 800;
    color: #0f3460;
    text-align: center;
    letter-spacing: -0.5px;
    margin-bottom: 0.1rem;
}

/* العنوان الفرعي */
.sub-title {
    font-size: 0.9rem;
    color: #6c757d;
    text-align: center;
    margin-bottom: 0.5rem;
}

/* بطاقة النتيجة */
.result-implicit {
    background: linear-gradient(135deg, #d4edda, #c3e6cb);
    border-left: 5px solid #28a745;
    border-radius: 10px;
    padding: 1.2rem 1.5rem;
    margin-top: 1rem;
}

.result-explicit {
    background: linear-gradient(135deg, #fff3cd, #ffeeba);
    border-left: 5px solid #ffc107;
    border-radius: 10px;
    padding: 1.2rem 1.5rem;
    margin-top: 1rem;
}

/* بطاقة المقياس */
.metric-card {
    background: #f8f9fa;
    border-radius: 10px;
    padding: 0.8rem 1rem;
    text-align: center;
    border: 1px solid #e9ecef;
    margin-bottom: 0.5rem;
}

.metric-value {
    font-size: 1.8rem;
    font-weight: 700;
    color: #0f3460;
}

.metric-label {
    font-size: 0.75rem;
    color: #6c757d;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

/* badge */
.badge {
    display: inline-block;
    padding: 0.2rem 0.6rem;
    border-radius: 20px;
    font-size: 0.75rem;
    font-weight: 600;
    margin: 0.1rem;
}

.badge-blue   { background:#dbeafe; color:#1d4ed8; }
.badge-green  { background:#dcfce7; color:#15803d; }
.badge-purple { background:#ede9fe; color:#7c3aed; }

/* قسم المعلومات */
.info-section {
    background: #f8f9fa;
    border-radius: 12px;
    padding: 1.2rem;
    margin-bottom: 1rem;
    border: 1px solid #e9ecef;
}

.section-title {
    font-size: 0.8rem;
    font-weight: 700;
    color: #6c757d;
    text-transform: uppercase;
    letter-spacing: 1px;
    margin-bottom: 0.6rem;
}
</style>
""", unsafe_allow_html=True)

# ═══════════════════════════════════════
# تحميل النموذج
# ═══════════════════════════════════════
@st.cache_resource
def load_model():
    return joblib.load('mon_modele_discursif.joblib')

model = load_model()

# ═══════════════════════════════════════
# الشريط الجانبي
# ═══════════════════════════════════════
with st.sidebar:
    st.markdown("""
    <div style='text-align:center; 
                padding: 1rem 0;'>
        <div style='font-size:2.5rem'>🧠</div>
        <div style='font-weight:700; 
                    font-size:1.1rem;
                    color:#0f3460;'>
            DiscourSense
        </div>
        <div style='font-size:0.75rem; 
                    color:#6c757d;'>
            ANNODIS · Master 2 SDL
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # المقاييس
    st.markdown(
        '<div class="section-title">'
        '📊 Performances du modèle'
        '</div>',
        unsafe_allow_html=True
    )

    metrics = [
        ("90%",  "Accuracy globale"),
        ("0.82", "F1 macro"),
        ("0.94", "F1 — Implicite"),
        ("0.70", "F1 — Explicite"),
        ("0.85", "F1 macro heuristique"),
    ]

    for value, label in metrics:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-value">{value}</div>
            <div class="metric-label">{label}</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # معلومات المذكرة
    st.markdown(
        '<div class="section-title">'
        '📋 À propos'
        '</div>',
        unsafe_allow_html=True
    )
    st.markdown("""
    <div style='font-size:0.82rem; 
                color:#495057;
                line-height:1.7;'>
        <b>Auteure :</b> Gourida Djihad<br>
        <b>Encadreur :</b> Dr. Selt Attia<br>
        <b>Université :</b> Ziane Achour, Djelfa<br>
        <b>Année :</b> 2025/2026
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # الشارات
    st.markdown(
        '<div class="section-title">'
        '🛠 Technologies'
        '</div>',
        unsafe_allow_html=True
    )
    badges = [
        ("Python",       "badge-blue"),
        ("scikit-learn", "badge-blue"),
        ("pandas",       "badge-green"),
        ("TF-IDF",       "badge-purple"),
        ("Streamlit",    "badge-green"),
        ("joblib",       "badge-blue"),
    ]
    badge_html = "".join([
        f'<span class="badge {cls}">{name}</span>'
        for name, cls in badges
    ])
    st.markdown(badge_html, unsafe_allow_html=True)

# ═══════════════════════════════════════
# العنوان الرئيسي
# ═══════════════════════════════════════
st.markdown(
    '<div class="main-title">'
    '🧠 DiscourSense'
    '</div>',
    unsafe_allow_html=True
)
st.markdown(
    '<div class="sub-title">'
    'Identification semi-automatique des relations '
    'discursives implicites · Corpus ANNODIS · '
    'Université Ziane Achour Djelfa'
    '</div>',
    unsafe_allow_html=True
)
st.markdown("---")

# ═══════════════════════════════════════
# التبويبات
# ═══════════════════════════════════════
tab1, tab2, tab3, tab4 = st.tabs([
    "🔍 Analyse en Direct",
    "📊 Résultats & Comparaison",
    "🔬 Analyse des Erreurs",
    "📚 Méthodologie"
])

# ───────────────────────────────────────
# Tab 1 — Analyse en Direct
# ───────────────────────────────────────
with tab1:
    st.markdown("### Tester le modèle sur deux segments")
    st.caption(
        "Saisissez deux segments textuels adjacents. "
        "Le modèle détermine si leur relation "
        "discursive est implicite ou explicite, "
        "et vous explique sa décision."
    )

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Segment 1**")
        s1 = st.text_area(
            label="s1",
            label_visibility="collapsed",
            placeholder="Ex : Le ciel est noir.",
            height=140
        )
    with col2:
        st.markdown("**Segment 2**")
        s2 = st.text_area(
            label="s2",
            label_visibility="collapsed",
            placeholder="Ex : Il va pleuvoir.",
            height=140
        )

    col_b1, col_b2, col_b3 = st.columns([3, 2, 3])
    with col_b2:
        analyser = st.button(
            "🔍 Analyser",
            use_container_width=True,
            type="primary"
        )

    if analyser:
        if s1.strip() and s2.strip():
            combined   = [s1.strip() + " " + s2.strip()]
            prediction = model.predict(combined)
            is_implicit = prediction[0] == 0

            if is_implicit:
                st.markdown(f"""
                <div class="result-implicit">
                    <div style='font-size:1.3rem;
                                font-weight:700;
                                color:#155724;'>
                        🟢 Relation IMPLICITE
                    </div>
                    <div style='margin-top:0.5rem;
                                color:#155724;'>
                        Aucun connecteur de surface 
                        n'a été détecté. Le lien 
                        logique entre les deux segments 
                        doit être inféré à partir du 
                        contenu sémantique et du 
                        contexte discursif.
                    </div>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div class="result-explicit">
                    <div style='font-size:1.3rem;
                                font-weight:700;
                                color:#856404;'>
                        🟡 Relation EXPLICITE
                    </div>
                    <div style='margin-top:0.5rem;
                                color:#856404;'>
                        Une marque linguistique 
                        (connecteur discursif) a été 
                        identifiée. La relation entre 
                        les segments est signalée 
                        directement dans le texte.
                    </div>
                </div>
                """, unsafe_allow_html=True)

            st.markdown("")
            col_d1, col_d2, col_d3 = st.columns(3)
            with col_d1:
                st.metric(
                    "Classe prédite",
                    "Implicite (0)" 
                    if is_implicit 
                    else "Explicite (1)"
                )
            with col_d2:
                st.metric(
                    "Connecteur détecté",
                    "Non" if is_implicit else "Oui"
                )
            with col_d3:
                st.metric(
                    "Confiance du modèle",
                    "LR weighted"
                )

            with st.expander(
                "📋 Détail de l'analyse"):
                st.markdown(f"""
                | Élément | Valeur |
                |---|---|
                | Segment 1 | {s1[:60]}... |
                | Segment 2 | {s2[:60]}... |
                | Classe prédite | 
                {'0 — Implicite' 
                 if is_implicit 
                 else '1 — Explicite'} |
                | Modèle utilisé | 
                Logistic Regression (TF-IDF) |
                | Corpus d'entraînement | 
                ANNODIS (1021 exemples) |
                """)

        else:
            st.error(
                "⚠️ Veuillez saisir les deux "
                "segments avant de lancer l'analyse."
            )

    st.markdown("---")
    st.markdown("**💡 Exemples à tester :**")
    col_e1, col_e2 = st.columns(2)
    with col_e1:
        st.info(
            "**Implicite :**\n\n"
            "S1 : *Le ciel est noir.*\n\n"
            "S2 : *Il va pleuvoir.*"
        )
    with col_e2:
        st.warning(
            "**Explicite :**\n\n"
            "S1 : *Il pleut,*\n\n"
            "S2 : ***donc** je reste.*"
        )

# ───────────────────────────────────────
# Tab 2 — Résultats & Comparaison
# ───────────────────────────────────────
with tab2:
    st.markdown("### Tâche 1 — Classification binaire")
    st.caption(
        "Régression logistique · TF-IDF · "
        "class_weight='balanced' · Split 80/20"
    )

    data_bin = {
        'Classe': [
            'Implicite (0)',
            'Explicite (1)',
            'Macro avg',
            'Weighted avg'
        ],
        'Précision': [0.95, 0.67, 0.81, 0.90],
        'Rappel':    [0.93, 0.73, 0.83, 0.90],
        'F1-Score':  [0.94, 0.70, 0.82, 0.90]
    }
    df_bin = pd.DataFrame(data_bin)
    st.table(df_bin.set_index('Classe'))

    col_g1, col_g2 = st.columns(2)
    with col_g1:
        st.markdown("**F1-Score par classe**")
        st.bar_chart(
            df_bin.set_index('Classe')['F1-Score'])
    with col_g2:
        st.markdown("**Précision vs Rappel**")
        df_pr = df_bin[
            df_bin['Classe'].isin(
                ['Implicite (0)', 'Explicite (1)']
            )
        ].set_index('Classe')[['Précision','Rappel']]
        st.bar_chart(df_pr)

    st.markdown("---")
    st.markdown(
        "### Tâche 2 — Classification multi-classes")
    st.caption(
        "5 groupes sémantiques · "
        "Comparaison des 4 classifieurs"
    )

    data_multi = {
        'Classifieur': [
            'Logistic Regression',
            'SVM (linear)',
            'Decision Tree',
            'Random Forest'
        ],
        'Accuracy': [0.395, 0.383, 0.356, 0.418],
        'F1 macro': [0.356, 0.344, 0.298, 0.251]
    }
    df_multi = pd.DataFrame(data_multi)

    col_m1, col_m2 = st.columns([1, 1])
    with col_m1:
        st.table(df_multi.set_index('Classifieur'))
    with col_m2:
        st.markdown("**F1 macro par classifieur**")
        st.bar_chart(
            df_multi.set_index(
                'Classifieur')['F1 macro'])

    st.markdown("---")
    st.markdown(
        "### Test de McNemar — "
        "Significativité statistique")

    col_mc1, col_mc2, col_mc3 = st.columns(3)
    with col_mc1:
        st.metric("Cas discordants", "26")
    with col_mc2:
        st.metric("Statistique de test", "0.039")
    with col_mc3:
        st.metric("p-value", "0.845")

    st.success(
        "✅ **Résultat :** La différence entre "
        "ML et Heuristique n'est **pas** "
        "statistiquement significative (p > 0.05). "
        "Les deux approches sont **complémentaires**, "
        "pas concurrentes."
    )

    st.markdown("---")
    st.markdown(
        "### Validation croisée (5-fold)")

    cv_data = {
        'Fold': ['Fold 1','Fold 2','Fold 3',
                 'Fold 4','Fold 5','Moyenne'],
        'F1 macro': [0.3472, 0.2996, 0.3698,
                     0.3807, 0.3522, 0.3499]
    }
    df_cv = pd.DataFrame(cv_data)

    col_cv1, col_cv2 = st.columns([1, 1])
    with col_cv1:
        st.table(df_cv.set_index('Fold'))
    with col_cv2:
        st.metric("Moyenne F1", "0.3499")
        st.metric("Écart-type", "0.0279")
        st.info(
            "Écart-type < 0.05 → "
            "Résultats **stables**")

    st.info(
        "**Note :** Les résultats multi-classes "
        "sont obtenus après regroupement des "
        "17 étiquettes originales d'ANNODIS "
        "en 5 groupes sémantiques. "
        "Ce regroupement a produit un gain "
        "de +14.7 points de F1 macro."
    )

# ───────────────────────────────────────
# Tab 3 — Analyse des Erreurs
# ───────────────────────────────────────
with tab3:
    st.markdown(
        "### Analyse des erreurs systématiques")
    st.caption(
        "155 erreurs sur 256 exemples de test "
        "(60.5%) — Logistic Regression · "
        "5 groupes sémantiques"
    )

    st.markdown("**Top 5 confusions**")
    data_err = {
        'Relation réelle': [
            'élaborative', 'temporelle',
            'temporelle', 'élaborative',
            'structurelle'
        ],
        'Relation prédite': [
            'temporelle', 'élaborative',
            'contrastive', 'causale',
            'élaborative'
        ],
        'Nb erreurs': [24, 20, 14, 14, 10],
        'Explication': [
            'Ordre chronologique apparent',
            'Développement thématique',
            'Connecteurs ambigus',
            'Développement ≈ causalité',
            'Fusion proche élaboration'
        ]
    }
    df_err = pd.DataFrame(data_err)
    st.table(df_err.set_index('Relation réelle'))

    st.markdown("---")
    st.markdown("**Exemples d'erreurs réelles**")

    exemples = [
        {
            "s1": "mais un ours polaire "
                  "leur fait peur.",
            "s2": "Les esquimaux s'enfuient...",
            "reel": "temporelle",
            "predit": "contrastive",
            "explication": "Le mot 'mais' en "
                           "début de segment "
                           "a trompé le modèle "
                           "— usage non connectif."
        },
        {
            "s1": "Dans les deux cas, le "
                  "lecteur doit chercher "
                  "des indices...",
            "s2": "La théorie repose sur "
                  "trois principes.",
            "reel": "élaborative",
            "predit": "causale",
            "explication": "La structure "
                           "argumentative ressemble "
                           "à une explication causale "
                           "sans en être une."
        },
        {
            "s1": "Le 20 juin 1789, les "
                  "députés se réunissent "
                  "dans la salle du Jeu "
                  "de paume,",
            "s2": "ils prêtent serment "
                  "de ne pas se séparer.",
            "reel": "causale",
            "predit": "temporelle",
            "explication": "La date en début "
                           "de segment active "
                           "une association "
                           "temporelle erronée."
        }
    ]

    for i, ex in enumerate(exemples):
        with st.expander(
            f"Exemple {i+1} — "
            f"Réel : **{ex['reel']}** → "
            f"Prédit : **{ex['predit']}**"
        ):
            col_x1, col_x2 = st.columns(2)
            with col_x1:
                st.markdown(
                    f"**Segment 1 :** {ex['s1']}")
                st.markdown(
                    f"**Segment 2 :** {ex['s2']}")
            with col_x2:
                st.error(
                    f"**Erreur :** "
                    f"{ex['reel']} → "
                    f"{ex['predit']}"
                )
                st.info(
                    f"**Explication :** "
                    f"{ex['explication']}"
                )

    st.markdown("---")
    st.markdown("**Baseline vs Notre modèle**")
    col_b1, col_b2, col_b3 = st.columns(3)
    with col_b1:
        st.metric(
            "Baseline naïf (F1 macro)",
            "0.116"
        )
    with col_b2:
        st.metric(
            "Notre modèle (F1 macro)",
            "0.356",
            delta="+0.240"
        )
    with col_b3:
        st.metric(
            "Gain vs baseline",
            "+24.1 points"
        )

# ───────────────────────────────────────
# Tab 4 — Méthodologie
# ───────────────────────────────────────
with tab4:
    st.markdown("### À propos de cette recherche")

    col_info1, col_info2 = st.columns(2)

    with col_info1:
        st.markdown("""
        <div class="info-section">
            <div class="section-title">
                📄 Mémoire
            </div>
            <div style='font-size:0.85rem;
                        line-height:1.8;'>
                <b>Titre :</b> Identification 
                semi-automatique des relations 
                discursives implicites dans un 
                corpus français annoté ANNODIS
                <br><br>
                <b>Filière :</b> Sciences du langage
                <br>
                <b>Niveau :</b> Master 2
                <br>
                <b>Auteure :</b> Gourida Djihad
                <br>
                <b>Encadreur :</b> Dr. Selt Attia
                <br>
                <b>Établissement :</b> 
                Université Ziane Achour, Djelfa
                <br>
                <b>Année :</b> 2025/2026
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col_info2:
        st.markdown("""
        <div class="info-section">
            <div class="section-title">
                📊 Corpus & Données
            </div>
            <div style='font-size:0.85rem;
                        line-height:1.8;'>
                <b>Corpus :</b> ANNODIS
                <br>
                <b>Volume :</b> 687 000 mots · 
                5 sous-corpus
                <br>
                <b>Instances :</b> 
                1 276 paires de segments
                <br>
                <b>Implicites :</b> 
                1 054 (82.6%)
                <br>
                <b>Explicites :</b> 
                222 (17.4%)
                <br>
                <b>Split :</b> 80% train / 20% test
                <br>
                <b>Validation :</b> 
                5-fold cross-validation
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### Pipeline méthodologique")

    steps = [
        ("1️⃣", "Extraction",
         "Parsing des fichiers .seg et .rel "
         "d'ANNODIS"),
        ("2️⃣", "Prétraitement",
         "Nettoyage, tokenisation, "
         "regroupement en 5 classes"),
        ("3️⃣", "Vectorisation",
         "TF-IDF (15 000 features, "
         "ngram 1-2, min_df=2)"),
        ("4️⃣", "Heuristique",
         "Lexique de connecteurs → "
         "détection implicite/explicite"),
        ("5️⃣", "ML supervisé",
         "LR · RF · DT · SVM · "
         "class_weight='balanced'"),
        ("6️⃣", "Évaluation",
         "F1 macro · McNemar · "
         "Cross-validation · Baseline"),
    ]

    col_s = st.columns(3)
    for i, (icon, title, desc) in enumerate(steps):
        with col_s[i % 3]:
            st.markdown(f"""
            <div class="info-section">
                <div style='font-size:1.5rem;
                            text-align:center;'>
                    {icon}
                </div>
                <div style='font-weight:700;
                            text-align:center;
                            color:#0f3460;
                            margin:0.3rem 0;'>
                    {title}
                </div>
                <div style='font-size:0.8rem;
                            color:#6c757d;
                            text-align:center;'>
                    {desc}
                </div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### Références principales")
    refs = [
        "Péry-Woodley et al. (2011) — "
        "ANNODIS corpus",
        "Lin et al. (2009) — "
        "Penn Discourse Treebank",
        "Asher & Lascarides (2003) — "
        "Logics of Discourse (SDRT)",
        "Mann & Thompson (1988) — "
        "Rhetorical Structure Theory",
        "McNemar (1947) — "
        "Test statistique de comparaison",
    ]
    for ref in refs:
        st.markdown(f"- {ref}")