# Évolution des langages de programmation

## Introduction
Ce document présente un aperçu des langages de programmation, y compris des statistiques sur leur création au fil des années.

## Graphique des langages par ans
<div id="languageGraph"></div>

<div id="languageGraph"></div>

<script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
<script>
document.addEventListener('DOMContentLoaded', function() {
    fetch('data/languages_per_decade_data.json')
        .then(response => response.json())
        .then(data => {
            var trace = {
                x: data.x,
                y: data.y,
                type: 'bar'
            };

            var layout = {
                title: 'Nombre de langages créés par décennie',
                xaxis: {title: 'Décennie de création'},
                yaxis: {title: 'Nombre de langages'}
            };

            Plotly.newPlot('languageGraph', [trace], layout);
        })
        .catch(error => console.error('Error loading the graph data:', error));
});
</script>

[Source des données](/Benchmark_Languages.md)

## Conclusion
Ce rapport fournit une vue d'ensemble des langages de programmation et leur évolution au fil des années. Les graphiques et les tableaux présentés ici aident à visualiser ces informations de manière claire et concise.
