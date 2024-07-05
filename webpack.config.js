const path = require('path');

module.exports = {
    entry: {
        interdiode: ['./modersite_js/index.ts', './modersite_js/theme.scss']
    },
    devtool: 'source-map',
    output: {
        filename: 'js/main.js',
        path: path.resolve(__dirname, 'modersite/static'),
    },
    module: {
        rules: [
            {
                test: /\.tsx?$/,
                use: 'ts-loader',
                exclude: /node_modules/,
                generator: {
                    filename: 'js/[name].js[query]',
                },
            },
            {
                test: /\.scss$/,
                exclude: /node_modules/,
                type: 'asset/resource',
                generator: {
                    filename: 'css/[name].css[query]',
                },
                use: [
                    {
                        loader: 'sass-loader', options: {
                            sourceMap: true,
                        },

                    }
                ]
            },
            {
                test: /\.(png|svg|jpg|jpeg|gif)$/i,
                type: 'asset/resource',
            },
            {
                test: /\.(woff|woff2|eot|ttf|otf)$/i,
                type: 'asset/resource',
            },
        ],
    },
    resolve: {
        extensions: ['.ts', '.js'],
    },
};
